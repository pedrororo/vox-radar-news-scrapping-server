import json
from src.repository.adapters.postgres.models.view_proposta import ViewProposta
from src.utils.utils import Utils
 
class ViewPropostaRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'id_proposta': Utils.to_int(data['ID_PROPOSTA']),
        'uf_proponente': data['UF_PROPONENTE'],
        'munic_proponente': data['MUNIC_PROPONENTE'],
        'cod_munic_ibge': Utils.to_int(data['COD_MUNIC_IBGE']),
        'cod_orgao_sup': Utils.to_int(data['COD_ORGAO_SUP']),
        'desc_orgao_sup': data['DESC_ORGAO_SUP'],
        'natureza_juridica': data['NATUREZA_JURIDICA'],
        'nr_proposta': data['NR_PROPOSTA'],
        'dia_prop': Utils.to_int(data['DIA_PROP']),
        'mes_prop': Utils.to_int(data['MES_PROP']),
        'ano_prop': Utils.to_int(data['ANO_PROP']),
        'dia_proposta': Utils.format_date_br_to_universal(data['DIA_PROPOSTA']),
        'cod_orgao': Utils.to_int(data['COD_ORGAO']),
        'desc_orgao': data['DESC_ORGAO'],
        'modalidade': data['MODALIDADE'],
        'identif_proponente': Utils.to_int(data['IDENTIF_PROPONENTE']),
        'nm_proponente': data['NM_PROPONENTE'],
        'cep_proponente': data['CEP_PROPONENTE'],
        'endereco_proponente': data['ENDERECO_PROPONENTE'],
        'bairro_proponente': data['BAIRRO_PROPONENTE'],
        'nm_banco': data['NM_BANCO'],
        'situacao_conta': data['SITUACAO_CONTA'],
        'situacao_projeto_basico': data['SITUACAO_PROJETO_BASICO'],
        'sit_proposta': data['SIT_PROPOSTA'],
        'dia_inic_vigencia_proposta': Utils.format_date_br_to_universal(data['DIA_INIC_VIGENCIA_PROPOSTA']),
        'dia_fim_vigencia_proposta': Utils.format_date_br_to_universal(data['DIA_FIM_VIGENCIA_PROPOSTA']),
        'objeto_proposta': data['OBJETO_PROPOSTA'],
        'item_investimento': data['ITEM_INVESTIMENTO'],
        'enviada_mandataria': data['ENVIADA_MANDATARIA'],
        'vl_global_prop': Utils.to_float(data['VL_GLOBAL_PROP']),
        'vl_repasse_prop': Utils.to_float(data['VL_REPASSE_PROP']),
        'vl_contrapartida_prop': Utils.to_float(data['VL_CONTRAPARTIDA_PROP']),
        'json': json.dumps(data)
      })

    query = ViewProposta.insert_many(list).on_conflict(
                  conflict_target=[ViewProposta.id_proposta],
                  preserve=[ViewProposta.uf_proponente, 
                    ViewProposta.munic_proponente,
                    ViewProposta.cod_munic_ibge,
                    ViewProposta.cod_orgao_sup,
                    ViewProposta.desc_orgao_sup,
                    ViewProposta.natureza_juridica,
                    ViewProposta.nr_proposta,
                    ViewProposta.dia_prop,
                    ViewProposta.ano_prop,
                    ViewProposta.dia_proposta,
                    ViewProposta.cod_orgao,
                    ViewProposta.desc_orgao,
                    ViewProposta.modalidade,
                    ViewProposta.identif_proponente,
                    ViewProposta.nm_proponente,
                    ViewProposta.cep_proponente,
                    ViewProposta.endereco_proponente,
                    ViewProposta.bairro_proponente,
                    ViewProposta.nm_banco,
                    ViewProposta.situacao_conta,
                    ViewProposta.situacao_projeto_basico,
                    ViewProposta.sit_proposta,
                    ViewProposta.dia_inic_vigencia_proposta,
                    ViewProposta.dia_fim_vigencia_proposta,
                    ViewProposta.objeto_proposta,
                    ViewProposta.item_investimento,
                    ViewProposta.enviada_mandataria,
                    ViewProposta.vl_global_prop,
                    ViewProposta.vl_repasse_prop,
                    ViewProposta.vl_contrapartida_prop,
                    ViewProposta.json])

    query.execute()

    

    

 