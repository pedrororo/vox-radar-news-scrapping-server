import json
from src.repository.adapters.postgres.models.view_desembolso import ViewDesembolso
from src.utils.utils import Utils

class ViewDesembolsoRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'id_desembolso': Utils.to_int(data['ID_DESEMBOLSO']),
        'nr_convenio': Utils.to_int(data['NR_CONVENIO']),
        'dt_ult_desembolso': Utils.format_date_br_to_universal(data['DT_ULT_DESEMBOLSO']),
        'qtd_dias_sem_desembolso': Utils.to_int(data['QTD_DIAS_SEM_DESEMBOLSO']),
        'data_desembolso': Utils.format_date_br_to_universal(data['DATA_DESEMBOLSO']),
        'ano_desembolso': Utils.to_int(data['ANO_DESEMBOLSO']),
        'mes_desembolso': Utils.to_int(data['MES_DESEMBOLSO']),
        'nr_siafi': data['NR_SIAFI'],
        'vl_desembolsado': Utils.to_float(data['VL_DESEMBOLSADO']),
        'json': json.dumps(data)
      })

      query = ViewDesembolso.insert_many(list)

    query.execute()

  def truncate(self):
    print('Truncate table')
    ViewDesembolso.truncate_table(restart_identity=True)
    