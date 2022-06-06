import json
import datetime
import pandas as pd
import datetime
from src.config.enum import Log

from src.integration.s3.s3 import S3
from src.integration.sqs.sqs import Sqs
from src.repository.adapters.postgres.view_cidadania_log_repository import ViewCidadaniaLogRepository
from src.types.sigarp_save_data_cidadania_queue_dto import SigarpSaveDataCidadaniaQueueDTO

from ..config.envs import Envs
from ..config.constants import Constants
from ..domain.base.base_service import BaseService
from ..types.sigarp_capture_data_cidadania_scrapping_queue_dto import SigarpCaptureDataCidadaniaScrappingQueueDTO
from ..types.return_service import ReturnService
import xlrd

from ..integration.selenium.selenium import Selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pandas as pd
import pickle
import time
import os

class CaptureDataCidadaniaScrappingService(BaseService):
    s3: S3
    sqs: Sqs
    selenium:Selenium = None
    state_dict = {
        'AC': 1, 'AL': 2, 'AM': 3, 'AP': 4,
        'BA': 5, 'CE': 6, 'DF': 7, 'ES': 8,
        'GO': 9, 'MA': 10, 'MG': 11, 'MS': 12,
        'MT': 13, 'PA': 14, 'PB': 15, 'PE': 16,
        'PI': 17, 'PR': 18, 'RJ': 19, 'RN': 20,
        'RO': 21, 'RR': 22, 'RS': 23, 'SC': 24,
        'SE': 25, 'SP': 26, 'TO': 27
    }

    def __init__(self):
        super().__init__()
        self.log_repository = ViewCidadaniaLogRepository()
        self.selenium = Selenium('cidadania')
        self.s3 = S3()
        self.sqs = Sqs()

    def exec(self, body:str) -> ReturnService:
        print(f'\n----- Scrapper | Init - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")} -----\n')
        
        sigarp_capture_data_cidadania_scrapping_queue_dto:SigarpCaptureDataCidadaniaScrappingQueueDTO = self.__parse_body(body)

        self.log(None, f"Iniciando scrapping estado de {sigarp_capture_data_cidadania_scrapping_queue_dto.state}, cidade de {sigarp_capture_data_cidadania_scrapping_queue_dto.city}, ano {sigarp_capture_data_cidadania_scrapping_queue_dto.year}", Log.INFO)

        state = sigarp_capture_data_cidadania_scrapping_queue_dto.state.upper()
        state_id = self.state_dict[state]
        city = sigarp_capture_data_cidadania_scrapping_queue_dto.city.upper()
        year = sigarp_capture_data_cidadania_scrapping_queue_dto.year
        
        response = LoginHandler(self.selenium.driver).make_login("https://sigtv.cidadania.gov.br")
        if response is False:
            self.log(None, "Não foi possível fazer Login, verificar se o site está online, ou se as credenciais estão corretas", Log.ERROR)
            self.selenium.driver.close()
            return ReturnService(False, 'Unsuccessful')
        else:
            print("Login bem-sucedido")

        response = PageHandler(self.selenium.driver).choose_page()
        if response is False:
            self.log(None, "Algo deu errado ao escolher a página correta para selecionar os dados", Log.ERROR)
            self.selenium.driver.close()
            return ReturnService(False, 'Unsuccessful')
        else:
            print("Página correta selecionada")
     
        search_funct = SearchHandler(self.selenium.driver, state_id, city, year) #O Estado de Minas Gerais está selecionado dentro do Método "State"
       
        response = search_funct.select_year()
        if response is False:
            self.log(None, f"Não foi possível escolher o Ano: {city}, {year}", Log.ERROR)
            self.selenium.driver.close()
            return ReturnService(False, 'Unsuccessful')
            
        response = search_funct.set_search()
        if response is False:
            self.log(None, f"Não foi possível inserir os dados da pesquisa: {city}, {year}", Log.ERROR)
            self.selenium.driver.close()   
            return ReturnService(False, 'Unsuccessful')        

        response = search_funct.select_city()
        if response is False:
            self.log(None, f"Não foi possível selecionar a cidade: {city}, {year}", Log.ERROR)
            self.selenium.driver.close()
            return ReturnService(False, 'Unsuccessful')
            
        Selenium.delay(1)
        response = search_funct.press_go()
        if response is False:
            self.log(None, f"Não foi possível clicar em GO: {city}, {year}", Log.ERROR)
            self.selenium.driver.close()
            return ReturnService(False, 'Unsuccessful')
 
        Selenium.delay(2)
        info = InfoHandle(self.selenium.driver)
        result = info.get_info()
        if not result:
            self.log(None, f"Nenhum dados encontrado para {sigarp_capture_data_cidadania_scrapping_queue_dto.state}, cidade de {sigarp_capture_data_cidadania_scrapping_queue_dto.city}, ano {sigarp_capture_data_cidadania_scrapping_queue_dto.year}", Log.INFO)
            self.selenium.driver.close()
            return ReturnService(True, 'Sucess')

        df = self.__add_column_dataframe(result[0], year)

        files_download = self.__save_json(df, state, city, year, result[1])
        self.__send_queue(files_download)

        self.log(None, f"Finalizando scrapping estado de {sigarp_capture_data_cidadania_scrapping_queue_dto.state}, cidade de {sigarp_capture_data_cidadania_scrapping_queue_dto.city}, ano {sigarp_capture_data_cidadania_scrapping_queue_dto.year}", Log.INFO)

        self.selenium.driver.close()
        return ReturnService(True, 'Sucess')

    def __parse_body(self, body:str) -> SigarpCaptureDataCidadaniaScrappingQueueDTO:
        body = json.loads(body)
        return SigarpCaptureDataCidadaniaScrappingQueueDTO(body.get('state'), body.get('city'), body.get('year'))

    def __add_column_dataframe(self, df, year):
        df2=df.assign(ANO=year)
        return df2
    
    def __save_json(self, df, state, city, year, file):
        total = len(df)

        print(f'----- Count rows {total} -----')

        file_name = f'cidadania/cidadania_{state}_{city}_{year}_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%z")}'.lower()
        self.s3.upload_file(file, Constants.S3['BUCKET']['SIGARP'], f'{file_name}_full.xlsx')

        result = df.to_json(orient='records')
        dataParsed = json.loads(result)
        count = 1
        list_chunk = 1
        files_list = []
        list_line = []
        chunk_num = 1

        for line in dataParsed:
            list_line.append(line)

            if(list_chunk == Constants.CHUNK[0]['JSON'] or count == total):
                print(f'Saving data {list_chunk}')
                chunk_file_name = f'{file_name}_{chunk_num}.json'
                self.s3.upload_file(json.dumps(list_line, ensure_ascii=False), Constants.S3['BUCKET']['SIGARP'], chunk_file_name)
                files_list.append(chunk_file_name)
                list_line = []
                list_chunk = 1
                chunk_num += 1

            count += 1
            list_chunk += 1
        
        return files_list
    
    def __send_queue(self, files_download:list):
        sigarp_save_data_cidadania_dto:SigarpSaveDataCidadaniaQueueDTO = SigarpSaveDataCidadaniaQueueDTO(files_download)
        
        self.log(None, 'Send to queue {} | {}'.format(Envs.AWS['SQS']['QUEUE']['SIGARP_SAVE_DATA_CIDADANIA'], sigarp_save_data_cidadania_dto.to_json()), Log.INFO)

        self.sqs.send_message_queue(Envs.AWS['SQS']['QUEUE']['SIGARP_SAVE_DATA_CIDADANIA'], sigarp_save_data_cidadania_dto.to_json())


class LoginHandler:
    LOGIN = "83035605653"
    PASSWORD = r"12Leiloca@"
    Path(f"temp/cidadania").mkdir(parents=True, exist_ok=True)
    COOKIE_FILE = "temp/cidadania/cookie.pickle"

    def __init__(self, driver):
        self.driver = driver
    
    def __fill_fields(self):
        try:
            login_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='cpf']")))
            login_field.send_keys(self.LOGIN)
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o botão de Login")
            return False
        try:
            password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
            password_field.send_keys(self.PASSWORD)
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o botão da Senha")
            return False
        return True      

    def __enter_login(self):
        try:
            enter_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            enter_field.click()
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o botão para entrar no site")
            return False
        return True

    def __check_if_logged(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='m-r-sm text-muted nome-cpf']")))
        except TimeoutException:
            print("Não fez Login no site")
            return False
        return True

    def __retrieve_url(self):
        return self.driver.current_url

    def __save_cookie(self):
        with open(self.COOKIE_FILE, 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)

    def __load_cookie(self):
        with open(self.COOKIE_FILE, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def __check_cookie_login(self):
        current_url = self.__retrieve_url()
        print(current_url)
        if current_url == "https://sigtv.cidadania.gov.br/login":
            return False
        else:
            return True

    def __login(self, site):
        for _ in range(3):
            self.driver.get(site)
            response = self.__fill_fields()
            if response is False:
                continue
            Selenium.delay(1)
            response = self.__enter_login()
            if response is False:
                continue           
            response = self.__check_if_logged()
            if response is False:
                continue
            if response is True:
                return response
        return response

    def make_login(self, site):
        cookie_exist = os.path.isfile(self.COOKIE_FILE)
        if not cookie_exist:
            print("Ainda não existem cookies de Login, vamos criá-los")
            response = self.__login(site)
            if response is False:
                print("Não foi possível fazer login")
                return response
            else:
                self.__save_cookie()
                print("Login realizado com sucesso. Cookies foram salvos")
                return response
        else:
            self.driver.get(site)
            self.__load_cookie()
            self.driver.refresh()
            self.driver.get(site)
            logged_in = self.__check_cookie_login()
            if logged_in:
                print("Cookies aplicados com sucesso")
                return True
            else:
                os.remove(self.COOKIE_FILE)
                response = self.__login(site)
                if response is False:
                    print("Não foi possível fazer login")
                    return response
                else:
                    self.__save_cookie()
                    print("Login realizado com sucesso. Cookies foram salvos")
                    return response


class PageHandler:
    def __init__(self, driver):
        self.driver = driver

    def __access_correct_page(self):
        try:
            espelhos_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Espelho')]")))
            espelhos_field.click()
        except (TimeoutException, Exception):
            print("Não conseguiu clicar no item Espelho")
            return False        
        try:
            espelhos_prog_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Espelho da Programação')]")))
            espelhos_prog_field.click()
        except (TimeoutException, Exception):
            print("Não conseguiu clicar no item Espelho da Programação")
            return False
        return True
    
    def __check_correct_page(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Espelho das Programações')]")))
        except TimeoutException:
            print("Não encontrou a página correta")
            return False
        return True

    def choose_page(self):
        for _ in range(5):
            response = self.__access_correct_page()
            if response is False:
                self.driver.refresh()
                continue
            response = self.__check_correct_page()
            if response is False:
                self.driver.refresh()
                continue
            else:
                return response
        return response
    

class SearchHandler:
    def __init__(self, driver, state_id:int, city:str, year:int):
        self.driver = driver
        self.state_id = state_id
        self.city = city
        self.year = year

    def select_year(self):
        try:
            year_search_bar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='ano']")))
            year_search_bar.click()
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o campo de busca do Ano")
            return False
        
        try:
           select_year = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(),'{self.year}')]")))
           select_year.click()         
        except (TimeoutException, Exception):
            print(f"Não conseguimos clicar no ano {self.year}")
            return False
        return True

    def select_esfera(self):
        try:
            state_filter = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='esfera']")))
            state_filter.click()
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o campo de busca das Esferas")
            return False
        Selenium.delay(1)
        try:
            select_municipio = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='MUNICIPAL']")))
            select_municipio.click()
        except (TimeoutException, Exception):
            print("Não conseguimos selecionar 'Municipio'")
            return False
        return True

    def select_state(self):
        try:            
            state_filter = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='uf']")))
            state_filter.click()
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o campo de busca do Estado")
            return False
        Selenium.delay(1)
        try:
            #A opção "11" no XPATH é referente ao Estado de Minas Gerais, caso queira selecionar outros Estados é preciso encontrar o ID na lista
            select_estado = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//option[@value='{self.state_id}']")))
            select_estado.click()
        except (TimeoutException, Exception):
            print("Não conseguimos selecionar o Estado")
            return False
        return True

    def select_city(self):   
        try:
            city_search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='municipio']")))
            city_search_bar.click()
        except (TimeoutException, Exception):
            print("Não conseguimos encontrar o campo de busca da Cidade")
            return False        
        Selenium.delay(1)

        try:
           select_city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(),'{self.city}')]")))  
           #self.driver.execute_script("arguments[0].scrollIntoView(true);", select_city)  
           Selenium.delay(2)
           select_city.click()
           #self.driver.execute_script("arguments[0].click();", select_city)
        except (TimeoutException, Exception):
            print(f"Não conseguimos clicar na Cidade {self.city}")
            return False
        return True

    def press_go(self):
        try:
            city_search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='btnPesquisarPorAnoLi']")))
            city_search_bar.click()
        except (TimeoutException, Exception):
            print("Não conseguimos clicar para Pesquisar")
            return False        
        return True        
    
    def set_search(self):
        response = self.select_esfera()
        if response is False:
            return response
        response = self.select_state()
        if response is False:
            return response
        return True

class InfoHandle:
    dir_path = os.path.abspath('temp/cidadania')
    def __init__(self, driver):
        self.driver = driver

    def __check_table(self):
        try:            
            table = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//table[@id='tb_ListaProgramacaoPorAno']//tbody//tr//td[1]")))
            response = table.text
            if response == "Nenhum registro encontrado":
                print(response)
                return False
        except TimeoutException:
            print("Não foi possível encontrar a Tabela, algo deu errado")
            return False
        return True

    def __click_download_excel(self):
        try:
            download_excel_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-file-excel-o fa-2x text-success']")))
        except TimeoutException:
            print("Não conseguimos clicar no Download da aba Cientes")
            return False
        self.driver.execute_script("arguments[0].click();", download_excel_button)
        return True

    def __find_excel(self, last_mod_time:float):
        start_time = time.time()
        while True:
            files = os.listdir(self.dir_path)
            for f in files:
                file_mod_time = os.path.getmtime(f"{self.dir_path}/{f}")
                if file_mod_time > last_mod_time and f == "Espelho.xlsx":
                    path = self.dir_path + "/" + str(f)
                    return path
            Selenium.delay(0.05)        
            elapsed_time = time.time() - start_time
            if elapsed_time >= 20:
                print(f"Não foi possível encontrar o arquivo na Pasta")
                return False

    def __get_file(self, path):
        return open(path,'rb')

    def __get_dataframe(self, path):        
        book = xlrd.open_workbook(path)
        sh = book.sheet_by_index(0)

        xlsx_dict = {sh.cell_value(rowx=0, colx=i): []
                    for i in range(sh.ncols)}

        for i in range(1, sh.nrows):
            for n, (k, v) in enumerate(xlsx_dict.items()):
                v.append(sh.cell_value(rowx=i, colx=n))

        column_names = ['TIPO_DOCUMENTO', 
            'NUMERO_DOCUMENTO', 
            'PARLAMENTAR_AUTOR', 
            'UF', 
            'MUNICIPIO',
            'NUMERO_PROGRAMACAO', 
            'GND_COD', 
            'VALOR_PROGRAMACAO', 
            'NOTA_EMPENHO', 
            'DATA_EMPENHO', 
            'ORDEM_BANCARIA', 
            'DATA_OB', 
            'SITUACAO_PROGRAMACAO']

        df = pd.DataFrame.from_dict(xlsx_dict)        
        df = df.set_axis(column_names, axis='columns', inplace=False)
        # df[['NUMERO_DOCUMENTO',
        #     'NUMERO_PROGRAMACAO', 
        #     'ORDEM_BANCARIA',
        #     'GND_COD']] = df[['NUMERO_DOCUMENTO',
        #         'NUMERO_PROGRAMACAO', 
        #         'ORDEM_BANCARIA',
        #         'GND_COD']].astype(int, errors='ignore')
        
        return df

    def get_info(self):
        response = self.__check_table()
        if response is False:
            return response
        #Listando todos os arquivos na pasta, ele irá verificar o último que foi modificado que tem o final .xlsx
        #E retornará o path para esse arquivo. 
        files_before = os.listdir(self.dir_path)
        time_files_before = [os.path.getmtime(f"{self.dir_path}/{i}") for i in files_before if i == "Espelho.xlsx"]
        try:
            last_modification = float(sorted(time_files_before, reverse=True)[0])
        except Exception:
            last_modification = 0
        if response is False:
            return False
        response = self.__click_download_excel()
        if response is False:
            return False
        path = self.__find_excel(last_modification)
        file = self.__get_file(path)
        if path is False:
            return False
        df = self.__get_dataframe(path)

        return [df, file]