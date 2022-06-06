from abc import abstractmethod
import json
from src.types.log_dto import LogDTO

class LogRepositoryInterface:
  
  @abstractmethod
  def add_log(self, log_dto: LogDTO):
    pass
