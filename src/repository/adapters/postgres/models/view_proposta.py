from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewProposta(BaseModel):
    id = IntegerField()
    id_proposta = BigIntegerField(primary_key=True)
    uf_proponente = CharField()
    munic_proponente = CharField()
    cod_munic_ibge = IntegerField()
    cod_orgao_sup = IntegerField()
    desc_orgao_sup = CharField()
    natureza_juridica = CharField()	
    nr_proposta = CharField()
    dia_prop = IntegerField()
    mes_prop = IntegerField()
    ano_prop = IntegerField()
    dia_proposta = DateField()	
    cod_orgao = IntegerField()
    desc_orgao = CharField()
    modalidade = CharField()
    identif_proponente = BigIntegerField()
    nm_proponente = CharField()
    cep_proponente = CharField()
    endereco_proponente = CharField()
    bairro_proponente = CharField()
    nm_banco = CharField()
    situacao_conta = CharField()
    situacao_projeto_basico = CharField()
    sit_proposta = CharField()
    dia_inic_vigencia_proposta = DateField()
    dia_fim_vigencia_proposta = DateField()
    objeto_proposta = CharField()
    item_investimento = CharField()
    enviada_mandataria = CharField()
    vl_global_prop = DecimalField()
    vl_repasse_prop = DecimalField()
    vl_contrapartida_prop = DecimalField()
    json = CharField()
  
    class Meta:
        db_table = 'view_propostas'

