import json
from src.repository.adapters.postgres.models.view_empenho import ViewEmpenho
from src.utils.utils import Utils

class ViewEmpenhoRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'id_empenho': Utils.to_int(data['ID_EMPENHO']),
        'nr_convenio': Utils.to_int(data['NR_CONVENIO']),
        'nr_empenho': data['NR_EMPENHO'],
        'tipo_nota': Utils.to_int(data['TIPO_NOTA']),
        'desc_tipo_nota': data['DESC_TIPO_NOTA'],
        'data_emissao': Utils.format_date_br_to_universal(data['DATA_EMISSAO']),
        'cod_situacao_empenho': data['COD_SITUACAO_EMPENHO'],
        'desc_situacao_empenho': data['DESC_SITUACAO_EMPENHO'],
        'valor_empenho': Utils.to_float(data['VALOR_EMPENHO']),
        'json': json.dumps(data)
      })

    query = ViewEmpenho.insert_many(list)
    query.execute()
  
  def truncate(self):
    print('Truncate table')
    ViewEmpenho.truncate_table(restart_identity=True)
    

    

 