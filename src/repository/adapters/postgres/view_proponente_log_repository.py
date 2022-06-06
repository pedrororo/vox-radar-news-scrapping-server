from src.repository.adapters.postgres.models.view_proponente_log import ViewProponenteLog
from src.types.view_proponente_log_dto import ViewProponenteLogDTO
 
class ViewProponenteLogRepository:

  def add_log(self, view_proponente_log_dto:ViewProponenteLogDTO):
    view_proponente_log = ViewProponenteLog()
    view_proponente_log.log = view_proponente_log_dto.log
    view_proponente_log.save()
