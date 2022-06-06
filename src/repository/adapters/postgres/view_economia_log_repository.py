from src.repository.adapters.postgres.models.view_economia_log import ViewEconomiaLog
from src.types.view_economia_log_dto import ViewEconomiaLogDTO
 
class ViewEconomiaLogRepository:

  def add_log(self, view_economia_log_dto:ViewEconomiaLogDTO):    
    view_economia_log = ViewEconomiaLog()
    view_economia_log.log = view_economia_log_dto.log
    view_economia_log.save()
