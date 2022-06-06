from src.repository.adapters.postgres.models.view_senador_log import ViewSenadorLog
from src.types.view_senador_log_dto import ViewSenadorLogDTO
 
class ViewSenadorLogRepository:

  def add_log(self, view_senador_log_dto:ViewSenadorLogDTO):
    view_senador_log = ViewSenadorLog()
    view_senador_log.log = view_senador_log_dto.log
    view_senador_log.save()
