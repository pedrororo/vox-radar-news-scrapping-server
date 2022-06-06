from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class Licitacao(BaseModel):
    id_licitacao = CharField(primary_key=True)
    nr_convenio = CharField()
    nr_licitacao = CharField()
    modalidade_licitacao = CharField()
    tp_processo_compra = CharField()
    tipo_licitacao = CharField()
    nr_processo_licitacao = CharField()	
    data_publicacao_licitacao = CharField()
    data_abertura_licitacao = CharField()
    data_encerramento_licitacao = CharField()
    data_homologacao_licitacao = CharField()
    status_licitacao = CharField()	
    situacao_aceite_processo_execu = CharField()
    sistema_origem = CharField()
    situacao_sistema = CharField()
    valor_licitacao = CharField()
   
    class Meta:
        db_table = 'licitacao'

