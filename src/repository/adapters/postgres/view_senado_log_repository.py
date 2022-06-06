from src.repository.adapters.postgres.models.view_senado_log import ViewSenadoLog
from src.types.view_senado_log_dto import ViewSenadoLogDTO
 
class ViewSenadoLogRepository:

  def add_log(self, view_senado_log_dto:ViewSenadoLogDTO):    
    view_senado_log = ViewSenadoLog()
    view_senado_log.log = view_senado_log_dto.log
    view_senado_log.save()
