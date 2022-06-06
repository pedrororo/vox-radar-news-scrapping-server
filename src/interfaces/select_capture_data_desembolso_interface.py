from abc import abstractmethod

from src.repository.adapters.postgres.view_desembolso_log_repository import ViewDesembolsoLogRepository
from src.repository.adapters.postgres.view_desembolso_repository import ViewDesembolsoRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class SelectCaptureDataDesembolsoInterface:
  view_desembolso_repository:ViewDesembolsoRepository
  view_desembolso_log_repository:ViewDesembolsoLogRepository
  sqs:Sqs
  s3:S3


  
  
