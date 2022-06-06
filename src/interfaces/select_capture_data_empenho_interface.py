from abc import abstractmethod

from src.repository.adapters.postgres.view_empenho_log_repository import ViewEmpenhoLogRepository
from src.repository.adapters.postgres.view_empenho_repository import ViewEmpenhoRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class SelectCaptureDataEmpenhoInterface:
  view_empenho_repository:ViewEmpenhoRepository
  view_empenho_log_repository:ViewEmpenhoLogRepository
  sqs:Sqs
  s3:S3


  
  
