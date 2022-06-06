from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class Pagamento(BaseModel):
    nr_mov_fin = CharField(primary_key=True)
    nr_convenio = CharField()
    identif_fornecedor = CharField()	
    nome_fornecedor = CharField()	
    tp_mov_financeira	= CharField()
    data_pag = CharField()
    nr_dl = CharField()	
    desc_dl = CharField()
    vl_pago = CharField()	

    class Meta:
        db_table = 'pagamento'
