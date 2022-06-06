from src.repository.adapters.postgres.models.view_proposta_log import ViewPropostaLog
from src.types.view_proposta_log_dto import ViewPropostaLogDTO
 
class ViewPropostaLogRepository:

  def add_log(self, view_proposta_log_dto:ViewPropostaLogDTO):
    view_proposta_log = ViewPropostaLog()
    view_proposta_log.log = view_proposta_log_dto.log
    view_proposta_log.save()
