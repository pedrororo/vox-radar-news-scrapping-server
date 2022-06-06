from abc import abstractmethod

from src.repository.adapters.postgres.view_convenio_log_repository import ViewConvenioLogRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class SelectCaptureDataConvenioInterface:
  view_convenio_log_repository:ViewConvenioLogRepository
  sqs:Sqs
  s3:S3


  
  
