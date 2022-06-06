from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class Emenda(BaseModel):
    id_proposta = CharField()
    qualif_proponente = CharField()
    cod_programa_emenda = CharField()
    nr_emenda = CharField()
    nome_parlamentar = CharField()
    beneficiario_emenda = CharField()
    ind_impositivo = CharField()
    tipo_parlamentar = CharField()
    valor_repasse_proposta_emenda = CharField()
    valor_repasse_emenda = CharField()

    class Meta:
        primary_key = False
        db_table = 'emenda'
