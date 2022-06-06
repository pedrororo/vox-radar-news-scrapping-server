from src.repository.adapters.postgres.models.view_saude_log import ViewSaudeLog
from src.types.view_saude_log_dto import ViewSaudeLogDTO
 
class ViewSaudeLogRepository:

  def add_log(self, view_saude_log_dto:ViewSaudeLogDTO):    
    view_saude_log = ViewSaudeLog()
    view_saude_log.log = view_saude_log_dto.log
    view_saude_log.save()
