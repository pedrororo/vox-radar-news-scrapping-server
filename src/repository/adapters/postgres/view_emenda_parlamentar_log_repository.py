from src.repository.adapters.postgres.models.view_emenda_parlamentar_log import ViewEmendaParlamentarLog
from src.types.view_emenda_parlamentar_log_dto import ViewEmendaParlamentarLogDTO
 
class ViewEmendaParlamentarLogRepository:

  def add_log(self, view_emenda_parlamentar_log_dto:ViewEmendaParlamentarLogDTO):
    view_emenda_parlamentar_log = ViewEmendaParlamentarLog()
    view_emenda_parlamentar_log.log = view_emenda_parlamentar_log_dto.log
    view_emenda_parlamentar_log.save()
