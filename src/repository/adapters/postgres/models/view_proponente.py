from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewProponente(BaseModel):
    identif_proponente = BigIntegerField(primary_key=True)
    nm_proponente = CharField()
    municipio_proponente = CharField()	
    uf_proponente = CharField()	
    endereco_proponente	= CharField()
    bairro_proponente = CharField()
    cep_proponente = CharField()	
    email_proponente = CharField()
    telefone_proponente = CharField()	
    fax_proponente = CharField()
    json = CharField()
  
    class Meta:
        db_table = 'view_proponentes'
