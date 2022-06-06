from src.repository.adapters.postgres.models.view_cidadania_log import ViewCidadaniaLog
from src.types.view_cidadania_log_dto import ViewCidadaniaLogDTO
 
class ViewCidadaniaLogRepository:

  def add_log(self, view_cidadania_log_dto:ViewCidadaniaLogDTO):    
    view_cidadania_log = ViewCidadaniaLog()
    view_cidadania_log.log = view_cidadania_log_dto.log
    view_cidadania_log.save()
