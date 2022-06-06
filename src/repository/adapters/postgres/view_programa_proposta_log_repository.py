from src.repository.adapters.postgres.models.view_programa_proposta_log import ViewProgramaPropostaLog
from src.types.view_programa_proposta_log_dto import ViewProgramaPropostaLogDTO
 
class ViewProgramaPropostaLogRepository:

  def add_log(self, view_programa_proposta_log_dto:ViewProgramaPropostaLogDTO):
    view_programa_proposta_log = ViewProgramaPropostaLog()
    view_programa_proposta_log.log = view_programa_proposta_log_dto.log
    view_programa_proposta_log.save()
