import json
from src.repository.adapters.postgres.models.view_proponente import ViewProponente
from src.utils.utils import Utils
 
class ViewProponenteRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      if(Utils.check_int(data['IDENTIF_PROPONENTE'])):
        list.append({
          'identif_proponente': Utils.to_int(data['IDENTIF_PROPONENTE']),
          'nm_proponente': data['NM_PROPONENTE'],
          'municipio_proponente': data['MUNICIPIO_PROPONENTE'],
          'uf_proponente': data['UF_PROPONENTE'],
          'endereco_proponente': data['ENDERECO_PROPONENTE'],
          'bairro_proponente': data['BAIRRO_PROPONENTE'],
          'cep_proponente': data['CEP_PROPONENTE'],
          'email_proponente': data['EMAIL_PROPONENTE'],
          'telefone_proponente': data['TELEFONE_PROPONENTE'],
          'fax_proponente': data['FAX_PROPONENTE'],
          'json': json.dumps(data)
        })

    query = ViewProponente.insert_many(list).on_conflict(
                  conflict_target=[ViewProponente.identif_proponente],
                  preserve=[ViewProponente.nm_proponente, 
                    ViewProponente.municipio_proponente,
                    ViewProponente.uf_proponente,
                    ViewProponente.endereco_proponente,
                    ViewProponente.bairro_proponente,
                    ViewProponente.cep_proponente,
                    ViewProponente.email_proponente,
                    ViewProponente.telefone_proponente,
                    ViewProponente.fax_proponente,
                    ViewProponente.json])

    query.execute()

    

    

 