from abc import abstractmethod
from src.integration.gov.senador_integration import SenadorIntegration
from src.repository.adapters.postgres.view_senador_log_repository import ViewSenadorLogRepository
from src.repository.adapters.postgres.view_parlamentar_repository import ViewParlamentarRepository

class SelectCaptureDataSenadorInterface:
  view_parlamentar_repository:ViewParlamentarRepository
  view_senador_log_repository:ViewSenadorLogRepository
  senador_integration: SenadorIntegration


  
  
