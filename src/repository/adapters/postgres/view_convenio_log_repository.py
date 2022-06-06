from src.repository.adapters.postgres.models.view_convenio_log import ViewConvenioLog
from src.types.view_convenio_log_dto import ViewConvenioLogDTO
 
class ViewConvenioLogRepository:

  def add_log(self, view_convenio_log_dto:ViewConvenioLogDTO):
    view_convenio_log = ViewConvenioLog()
    view_convenio_log.log = view_convenio_log_dto.log
    view_convenio_log.save()
