from src.repository.adapters.postgres.models.view_empenho_log import ViewEmpenhoLog
from src.types.view_empenho_log_dto import ViewEmpenhoLogDTO
 
class ViewEmpenhoLogRepository:

  def add_log(self, view_empenho_log_dto:ViewEmpenhoLogDTO):
    view_empenho_log = ViewEmpenhoLog()
    view_empenho_log.log = view_empenho_log_dto.log
    view_empenho_log.save()
