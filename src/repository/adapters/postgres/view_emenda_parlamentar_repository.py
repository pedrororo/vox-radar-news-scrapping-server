import json
from src.repository.adapters.postgres.models.view_emenda_parlamentar import ViewEmendaParlamentar
from src.utils.utils import Utils

class ViewEmendaParlamentarRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'acao_cod': data['ACAO_COD'],
        'acao_ajustada': data['ACAO_AJUSTADA'],
        'autor': data['AUTOR'].title(),
        'autor_tipo': data['AUTOR_TIPO'].title(),
        'uf_autor': data['AUTOR_UF'],
        'numero_emenda': Utils.to_int(data['EMENDA_NUMERO_ANO'].split('-')[0]),
        'gnd_cod': Utils.to_int(data['GND_COD']),
        'gnd': data['GND'],
        'localidade': data['LOCALIDADE'],
        'modalidade_aplicacao_cod': Utils.to_int(data['MODALIDADE_APLICACAO_COD']),
        'modalidade_aplicacao': data['MODALIDADE_APLICACAO'],
        'orgao_superior_uo': data['ORGAO_SUPERIOR_UO'],
        'orgao_superior_orcamentario_cod': Utils.to_int(data['ORGAO_SUPERIOR_ORCAMENTARIO_COD']),
        'uo_cod': Utils.to_int(data['UO_COD']),
        'uo_ajustada': data['UO_AJUSTADA'],
        'ano': Utils.to_int(Utils.to_int(data['EMENDA_ANO'])),
        'partido': data['PARTIDO'].upper(),
        'valor_autorizado': Utils.to_float(data['AUTORIZADO']),
        'valor_empenhado': Utils.to_float(data['EMPENHADO']),
        'valor_pago': Utils.to_float(data['PAGO']),
        'json': json.dumps(data)
      })

    query = ViewEmendaParlamentar.insert_many(list)
    query.execute()
  
  def truncate(self):
    print('Truncate table')
    ViewEmendaParlamentar.truncate_table(restart_identity=True)
    

    

 