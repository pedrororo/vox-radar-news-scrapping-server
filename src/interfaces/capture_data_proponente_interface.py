from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_proponente_log_repository import ViewProponenteLogRepository
from src.repository.adapters.postgres.view_proponente_repository import ViewProponenteRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class CaptureDataProponenteInterface:
  view_proponente_repository:ViewProponenteRepository
  view_proponente_log_repository:ViewProponenteLogRepository
  sqs:Sqs
  s3:S3


  
  
