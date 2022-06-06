from src.repository.adapters.postgres.models.view_programa_log import ViewProgramaLog
from src.types.view_programa_log_dto import ViewProgramaLogDTO
 
class ViewProgramaLogRepository:

  def add_log(self, view_programa_log_dto:ViewProgramaLogDTO):
    view_programa_log = ViewProgramaLog()
    view_programa_log.log = view_programa_log_dto.log
    view_programa_log.save()
