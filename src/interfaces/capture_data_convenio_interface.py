from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_convenio_log_repository import ViewConvenioLogRepository
from src.repository.adapters.postgres.view_convenio_repository import ViewConvenioRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class CaptureDataConvenioInterface:
  view_convenio_repository:ViewConvenioRepository
  view_convenio_log_repository:ViewConvenioLogRepository
  sqs:Sqs
  s3:S3


  
  
