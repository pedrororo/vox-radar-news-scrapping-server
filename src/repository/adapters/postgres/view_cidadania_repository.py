import json
from src.repository.adapters.postgres.models.view_cidadania import ViewCidadania
from src.utils.utils import Utils

class ViewCidadaniaRepository:

  def bulk_create(self, bulkData):
    list = []
 
    for data in bulkData:
      list.append({
        'tipo_documento': data['NR_CONVENIO'],
        'numero_documento': Utils.to_int(data['DT_ULT_DESEMBOLSO']),
        'parlamentar':data['QTD_DIAS_SEM_DESEMBOLSO'],
        'uf': data['DATA_DESEMBOLSO'],
        'municipio': data['ANO_DESEMBOLSO'],
        'numero_programacao': Utils.to_int(data['MES_DESEMBOLSO']),
        'gnd_cod': Utils.to_int(data['NR_SIAFI']),
        'valor_programacao': Utils.to_float(data['VL_DESEMBOLSADO']),
        'nota_empenho': Utils.to_int(data['VL_DESEMBOLSADO']),
        'data_empenho': Utils.format_date_br_to_universal(data['VL_DESEMBOLSADO']),
        'ordem_bancaria': Utils.to_int(data['VL_DESEMBOLSADO']),
        'data_ob': Utils.format_date_br_to_universal(data['VL_DESEMBOLSADO']),
        'situacao_programacao': data['VL_DESEMBOLSADO'],
        'json': json.dumps(data)
      })

      query = ViewCidadania.insert_many(list)

    query.execute()

  def truncate(self):
    print('Truncate table')
    ViewCidadania.truncate_table(restart_identity=True)
    