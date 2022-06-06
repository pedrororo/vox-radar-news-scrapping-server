from src.repository.adapters.postgres.models.view_desembolso_log import ViewDesembolsoLog
from src.types.view_desembolso_log_dto import ViewDesembolsoLogDTO
 
class ViewDesembolsoLogRepository:

  def add_log(self, view_desembolso_log_dto:ViewDesembolsoLogDTO):
    view_desembolso_log = ViewDesembolsoLog()
    view_desembolso_log.log = view_desembolso_log_dto.log
    view_desembolso_log.save()
