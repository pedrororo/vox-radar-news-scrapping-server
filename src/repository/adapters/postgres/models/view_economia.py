from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewEconomia(BaseModel):    
    id = IntegerField()
    tipo_documento = CharField()
    numero_documento = BigIntegerField()
    parlamentar = CharField()
    uf = CharField()
    municipio = CharField()
    numero_programacao = BigIntegerField()
    gnd_cod = IntegerField()	
    valor_programacao = DecimalField()
    nota_empenho = BigIntegerField()
    data_empenho = DateField()
    ordem_bancaria = BigIntegerField()
    data_ob = DateField()	
    situacao_programacao = CharField()
    json = CharField()

    class Meta:
        primary_key = False
        db_table = 'view_economia'
        # indexes = (
        #     (('nr_convenio', 'id_proposta'), True),  # Note the trailing comma!
        # )

