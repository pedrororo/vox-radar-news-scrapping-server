from src.repository.adapters.postgres.models.view_deputado_log import ViewDeputadoLog
from src.types.view_deputado_log_dto import ViewDeputadoLogDTO
 
class ViewDeputadoLogRepository:

  def add_log(self, view_deputado_log_dto:ViewDeputadoLogDTO):
    view_deputado_log = ViewDeputadoLog()
    view_deputado_log.log = view_deputado_log_dto.log
    view_deputado_log.save()
