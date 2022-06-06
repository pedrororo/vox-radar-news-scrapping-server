from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewPrograma(BaseModel):
    id = IntegerField()
    id_programa = BigIntegerField()
    cod_orgao_sup_programa = BigIntegerField()
    desc_orgao_sup_programa = CharField()
    cod_programa = BigIntegerField()
    nome_programa = CharField()
    sit_programa = CharField()	
    data_disponibilizacao = DateField()
    ano_disponibilizacao = IntegerField()
    dt_prog_ini_receb_prop = DateField()
    dt_prog_fim_receb_prop = DateField()
    dt_prog_ini_emenda_par = DateField()	
    dt_prog_fim_emenda_par = DateField()	
    dt_prog_ini_benef_esp = DateField()
    dt_prog_fim_benef_esp = DateField()
    modalidade_programa = CharField()
    natureza_juridica_programa = CharField()
    uf_programa = BigIntegerField()
    acao_orcamentaria = CharField()
    json = CharField()
    class Meta:
        primary_key = False
        db_table = 'view_programa'

