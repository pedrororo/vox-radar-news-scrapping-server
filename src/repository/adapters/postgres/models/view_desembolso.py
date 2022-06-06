from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewDesembolso(BaseModel):
    id = IntegerField()
    id_desembolso = BigIntegerField()
    nr_convenio = BigIntegerField()
    dt_ult_desembolso = DateField()
    qtd_dias_sem_desembolso = CharField()
    data_desembolso = DateField()
    ano_desembolso = IntegerField()
    mes_desembolso = IntegerField()
    nr_siafi = CharField()
    vl_desembolsado = DecimalField()
    json = CharField()
   
    class Meta:
        primary_key = False
        db_table = 'view_desembolso'