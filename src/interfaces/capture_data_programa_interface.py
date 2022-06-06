from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_programa_log_repository import ViewProgramaLogRepository
from src.repository.adapters.postgres.view_programa_repository import ViewProgramaRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class CaptureDataProgramaInterface:
  view_programa_repository:ViewProgramaRepository
  view_programa_log_repository:ViewProgramaLogRepository
  sqs:Sqs
  s3:S3


  
  
