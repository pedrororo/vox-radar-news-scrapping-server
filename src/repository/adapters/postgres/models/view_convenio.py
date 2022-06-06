from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewConvenio(BaseModel):    
    id = IntegerField()
    nr_convenio = BigIntegerField()
    id_proposta = BigIntegerField()
    dia = IntegerField()
    mes = IntegerField()
    ano = IntegerField()
    dia_assin_conv = DateField()
    sit_convenio = CharField()	
    subsituacao_conv = CharField()
    situacao_publicacao = CharField()
    instrumento_ativo = CharField()
    ind_opera_obtv = CharField()
    nr_processo = CharField()	
    ug_emitente = IntegerField()
    dia_publ_conv = DateField()
    dia_inic_vigenc_conv = DateField()
    dia_fim_vigenc_conv = DateField()
    dia_fim_vigenc_original_conv = DateField()
    dias_prest_contas = IntegerField()
    dia_limite_prest_contas = DateField()
    data_suspensiva = DateField()
    data_retirada_suspensiva = DateField()
    dias_clausula_suspensiva = IntegerField()
    situacao_contratacao = CharField()
    ind_assinado = CharField()
    motivo_suspensao = CharField()
    ind_foto = CharField()
    qtde_convenios = IntegerField()
    qtd_ta = IntegerField()
    qtd_prorroga = IntegerField()
    vl_global_conv = DecimalField()
    vl_repasse_conv = DecimalField()
    vl_contrapartida_conv = DecimalField()
    vl_empenhado_conv = DecimalField()
    vl_desembolsado_conv = DecimalField()
    vl_saldo_reman_tesouro = DecimalField()
    vl_saldo_reman_convenente = DecimalField()
    vl_rendimento_aplicacao = DecimalField()
    vl_ingresso_contrapartida = DecimalField()
    vl_saldo_conta = DecimalField()
    valor_global_original_conv = DecimalField()
    json = CharField()
    class Meta:
        primary_key = False
        db_table = 'view_convenios'
        indexes = (
            (('nr_convenio', 'id_proposta'), True),  # Note the trailing comma!
        )

