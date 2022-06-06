import json
from src.repository.adapters.postgres.models.view_convenio import ViewConvenio
from src.utils.utils import Utils

class ViewConvenioRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'nr_convenio': Utils.to_int(data['NR_CONVENIO']) if Utils.to_int(data['NR_CONVENIO']) else 0,
        'id_proposta': Utils.to_int(data['ID_PROPOSTA']) if Utils.to_int(data['ID_PROPOSTA']) else 0,
        'dia': Utils.to_int(data['DIA']),
        'mes': Utils.to_int(data['MES']),
        'ano': Utils.to_int(data['ANO']),
        'dia_assin_conv': Utils.format_date_br_to_universal(data['DIA_ASSIN_CONV']),
        'sit_convenio': data['SIT_CONVENIO'],
        'subsituacao_conv': data['SUBSITUACAO_CONV'],
        'situacao_publicacao': data['SITUACAO_PUBLICACAO'],
        'instrumento_ativo': data['INSTRUMENTO_ATIVO'],
        'ind_opera_obtv': data['IND_OPERA_OBTV'],
        'nr_processo': data['NR_PROCESSO'],
        'ug_emitente': Utils.to_int(data['UG_EMITENTE']),
        'dia_publ_conv': Utils.format_date_br_to_universal(data['DIA_PUBL_CONV']),
        'dia_inic_vigenc_conv': Utils.format_date_br_to_universal(data['DIA_INIC_VIGENC_CONV']),
        'dia_fim_vigenc_conv': Utils.format_date_br_to_universal(data['DIA_FIM_VIGENC_CONV']),
        'dia_fim_vigenc_original_conv': Utils.format_date_br_to_universal(data['DIA_FIM_VIGENC_ORIGINAL_CONV']),
        'dias_prest_contas': Utils.to_int(data['DIAS_PREST_CONTAS']),
        'dia_limite_prest_contas': Utils.format_date_br_to_universal(data['DIA_LIMITE_PREST_CONTAS']),
        'data_suspensiva': Utils.format_date_br_to_universal(data['DATA_SUSPENSIVA']),
        'data_retirada_suspensiva': Utils.format_date_br_to_universal(data['DATA_RETIRADA_SUSPENSIVA']),
        'dias_clausula_suspensiva': Utils.to_int(data['DIAS_CLAUSULA_SUSPENSIVA']),
        'situacao_contratacao': data['SITUACAO_CONTRATACAO'],
        'ind_assinado': data['IND_ASSINADO'],
        'motivo_suspensao': data['MOTIVO_SUSPENSAO'],
        'ind_foto': data['IND_FOTO'],
        'qtde_convenios': Utils.to_int(data['QTDE_CONVENIOS']),
        'qtd_ta': Utils.to_int(data['QTD_TA']),
        'qtd_prorroga': Utils.to_int(data['QTD_PRORROGA']),
        'vl_global_conv': Utils.to_float(data['VL_GLOBAL_CONV']),
        'vl_repasse_conv': Utils.to_float(data['VL_REPASSE_CONV']),
        'vl_contrapartida_conv': Utils.to_float(data['VL_CONTRAPARTIDA_CONV']),
        'vl_empenhado_conv': Utils.to_float(data['VL_EMPENHADO_CONV']),
        'vl_desembolsado_conv': Utils.to_float(data['VL_DESEMBOLSADO_CONV']),
        'vl_saldo_reman_tesouro': Utils.to_float(data['VL_SALDO_REMAN_TESOURO']),
        'vl_saldo_reman_convenente': Utils.to_float(data['VL_SALDO_REMAN_CONVENENTE']),
        'vl_rendimento_aplicacao': Utils.to_float(data['VL_RENDIMENTO_APLICACAO']),
        'vl_ingresso_contrapartida': Utils.to_float(data['VL_INGRESSO_CONTRAPARTIDA']),
        'vl_saldo_conta': Utils.to_float(data['VL_SALDO_CONTA']),
        'valor_global_original_conv': Utils.to_float(data['VALOR_GLOBAL_ORIGINAL_CONV']),
        'json': json.dumps(data)
      })

    query = ViewConvenio.insert_many(list).on_conflict(
                  conflict_target=[ViewConvenio.nr_convenio, ViewConvenio.id_proposta],
                  preserve=[ViewConvenio.dia,
                    ViewConvenio.mes,
                    ViewConvenio.ano,
                    ViewConvenio.dia_assin_conv,
                    ViewConvenio.sit_convenio,
                    ViewConvenio.subsituacao_conv,
                    ViewConvenio.situacao_publicacao,
                    ViewConvenio.instrumento_ativo,
                    ViewConvenio.ind_opera_obtv,
                    ViewConvenio.nr_processo,
                    ViewConvenio.ug_emitente,
                    ViewConvenio.dia_publ_conv,
                    ViewConvenio.dia_inic_vigenc_conv,
                    ViewConvenio.dia_fim_vigenc_conv,
                    ViewConvenio.dia_fim_vigenc_original_conv,
                    ViewConvenio.dias_prest_contas,
                    ViewConvenio.dia_limite_prest_contas,
                    ViewConvenio.data_suspensiva,
                    ViewConvenio.data_retirada_suspensiva,
                    ViewConvenio.dias_clausula_suspensiva,
                    ViewConvenio.situacao_contratacao,
                    ViewConvenio.ind_assinado,
                    ViewConvenio.motivo_suspensao,
                    ViewConvenio.ind_foto,
                    ViewConvenio.qtde_convenios,
                    ViewConvenio.qtd_ta,
                    ViewConvenio.qtd_prorroga,
                    ViewConvenio.vl_global_conv,
                    ViewConvenio.vl_repasse_conv,
                    ViewConvenio.vl_contrapartida_conv,
                    ViewConvenio.vl_empenhado_conv,
                    ViewConvenio.vl_desembolsado_conv,
                    ViewConvenio.vl_saldo_reman_tesouro,
                    ViewConvenio.vl_saldo_reman_convenente,
                    ViewConvenio.vl_rendimento_aplicacao,
                    ViewConvenio.vl_ingresso_contrapartida,
                    ViewConvenio.vl_saldo_conta,
                    ViewConvenio.valor_global_original_conv,
                    ViewConvenio.json])

    query.execute()
    

    

 