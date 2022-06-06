from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import importlib
import time
import numpy as np
from src.config.envs import Envs
from src.config.constants import Constants
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import os
from pathlib import Path

class Selenium:
  driver = None
  dir_path = None

  def __init__(self, folder_temp:str=None):
    if folder_temp:
      Path(f"temp/{folder_temp}").mkdir(parents=True, exist_ok=True)
      self.dir_path = os.path.abspath(f'temp/{folder_temp}')
    else:
      Path("temp").mkdir(exist_ok=True)
      self.dir_path = os.path.abspath(f'temp')

    self.driver = self.get_driver_chrome()

  def wait(self, timeout:int=10, poll_frequency:int=1):
    try:
      wait:WebDriverWait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
      return wait
    except Exception as err:
      print(err)
      raise err

  def get_driver_chrome(self):
    return self.__driver_chrome()

  def __driver_chrome(self):
    print('----- Attach driver layer -----')
    webdriver_manager = importlib.import_module("webdriver_manager.chrome")

    options = webdriver.ChromeOptions()

    if Envs.ENVIRONMENT[0] != Constants.ENVIRONMENT['LOCAL']:
      options.add_argument('--headless')

    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument(f'user-agent={self.__get_user_agent()}')

    driver = webdriver.Chrome(executable_path=webdriver_manager.ChromeDriverManager().install(), chrome_options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
    })

    params = {'behavior': 'allow', 'downloadPath': self.dir_path}
    driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

    user_agent = driver.execute_script("return navigator.userAgent")
    print(f'----- UserAgent - {user_agent} -----')
    return driver

  def __get_user_agent(self):
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    print(f'----- Selected UserAgent: {user_agent} -----')
    return user_agent

  @classmethod
  def delay(self, manual_delay:int=None):
    if(manual_delay):
        print(f'----- Delay of {manual_delay} seconds -----')
        time.sleep(manual_delay)    
    else:
        range_delays = [4, 5, 6, 7, 8]
        randon_dalay = np.random.choice(range_delays)
        print(f'----- Delay of {randon_dalay} seconds -----')
        time.sleep(randon_dalay)

  @classmethod
  def close(self):
    self.driver.close()
    self.driver.quit()
    print("Your browser has been closed")
    time.sleep(2)
