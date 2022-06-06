from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class HistoricoSituacao(BaseModel):
    id_proposta = CharField()
    nr_convenio = CharField()
    dia_historico_sit = CharField()
    historico_sit = CharField()
    dias_historico_sit = CharField()
    cod_historico_sit = CharField()

    class Meta:
        primary_key = False
        db_table = 'historico_situacao'
