import json
from src.repository.adapters.postgres.models.view_programa import ViewPrograma
from src.utils.utils import Utils

class ViewProgramaRepository:

  def bulk_create(self, bulkData):
    list = []

    for data in bulkData:
      list.append({
        'id_programa': Utils.to_int(data['ID_PROGRAMA']),
        'cod_orgao_sup_programa': Utils.to_int(data['COD_ORGAO_SUP_PROGRAMA']),
        'desc_orgao_sup_programa': data['DESC_ORGAO_SUP_PROGRAMA'],
        'cod_programa': Utils.to_int(data['COD_PROGRAMA']),
        'nome_programa': data['NOME_PROGRAMA'],
        'sit_programa': data['SIT_PROGRAMA'],
        'data_disponibilizacao': Utils.format_date_br_to_universal(data['DATA_DISPONIBILIZACAO']),
        'ano_disponibilizacao': Utils.to_int(data['ANO_DISPONIBILIZACAO']),
        'dt_prog_ini_receb_prop': Utils.format_date_br_to_universal(data['DT_PROG_INI_RECEB_PROP']),
        'dt_prog_fim_receb_prop': Utils.format_date_br_to_universal(data['DT_PROG_FIM_RECEB_PROP']),
        'dt_prog_ini_emenda_par': Utils.format_date_br_to_universal(data['DT_PROG_INI_EMENDA_PAR']),
        'dt_prog_fim_emenda_par': Utils.format_date_br_to_universal(data['DT_PROG_FIM_EMENDA_PAR']),
        'dt_prog_ini_benef_esp': Utils.format_date_br_to_universal(data['DT_PROG_INI_BENEF_ESP']),
        'dt_prog_fim_benef_esp': Utils.format_date_br_to_universal(data['DT_PROG_FIM_BENEF_ESP']),
        'modalidade_programa': data['MODALIDADE_PROGRAMA'],
        'natureza_juridica_programa': data['NATUREZA_JURIDICA_PROGRAMA'],
        'uf_programa': data['UF_PROGRAMA'],
        'acao_orcamentaria': data['ACAO_ORCAMENTARIA'],
        'json': json.dumps(data)
      })

    query = ViewPrograma.insert_many(list)

    query.execute()

  def truncate(self):
    print('Truncate table')
    ViewPrograma.truncate_table(restart_identity=True)
   