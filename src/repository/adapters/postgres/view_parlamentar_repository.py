import json
from src.repository.adapters.postgres.models.view_parlamentar import ViewParlamentar
from src.utils.utils import Utils

class ViewParlamentarRepository:

  def bulk_create(self, bulkData):
    query = ViewParlamentar.insert_many(bulkData).on_conflict(
                  conflict_target=[ViewParlamentar.parlamentar_id, ViewParlamentar.nome],
                  preserve=[ViewParlamentar.partido, 
                    ViewParlamentar.uf,
                    ViewParlamentar.email,
                    ViewParlamentar.foto,
                    ViewParlamentar.active,
                    ViewParlamentar.cargo,
                    ViewParlamentar.json])

    query.execute()

  def inactivate_all(self, cargo:str):
    print('----- Inactivate all -----')

    update = ViewParlamentar.update(active = False).where(ViewParlamentar.cargo == cargo)
    update.execute()

  



    

 