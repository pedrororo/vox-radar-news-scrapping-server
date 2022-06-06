from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewEmpenho(BaseModel):
    id = IntegerField()
    id_empenho = BigIntegerField()
    nr_convenio = BigIntegerField()
    nr_empenho = CharField()
    tipo_nota = IntegerField()
    desc_tipo_nota = CharField()
    data_emissao = DateField()
    cod_situacao_empenho = CharField()
    desc_situacao_empenho = CharField()
    valor_empenho = DecimalField()
    json = CharField()

    class Meta:
        primary_key = False
        db_table = 'view_empenho'
