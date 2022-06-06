from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewEmendaParlamentar(BaseModel):
    id = IntegerField()
    acao_cod = CharField()
    acao_ajustada = CharField()
    autor = CharField()
    autor_tipo = CharField()
    uf_autor = CharField()
    numero_emenda = BigIntegerField()
    gnd_cod = IntegerField()
    gnd = CharField()
    localidade = CharField()
    modalidade_aplicacao_cod = IntegerField()
    modalidade_aplicacao = CharField()
    orgao_superior_uo = CharField()
    orgao_superior_orcamentario_cod = IntegerField()
    uo_cod = IntegerField()
    uo_ajustada = CharField()
    ano = IntegerField()
    partido = CharField()
    valor_autorizado = DecimalField()
    valor_empenhado = DecimalField()
    valor_pago = DecimalField()
    json = CharField()

    class Meta:
        primary_key = False
        db_table = 'view_emenda_parlamentar'
