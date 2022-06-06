import json
from src.repository.adapters.postgres.models.view_programa_proposta import ViewProgramaProposta
from src.utils.utils import Utils

class ViewProgramaPropostaRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'id_programa': Utils.to_int(data['ID_PROGRAMA']),
        'id_proposta': Utils.to_int(data['ID_PROPOSTA']),
        'json': json.dumps(data)
      })

    query = ViewProgramaProposta.insert_many(list)

    query.execute()

  def truncate(self):
    print('Truncate table')
    ViewProgramaProposta.truncate_table(restart_identity=True)
   