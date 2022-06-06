from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_emenda_parlamentar_log_repository import ViewEmendaParlamentarLogRepository
from src.repository.adapters.postgres.view_emenda_parlamentar_repository import ViewEmendaParlamentarRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class CaptureDataEmendaParlamentarInterface:
  view_emenda_parlamentar_repository:ViewEmendaParlamentarRepository
  view_emenda_parlamentar_log_repository:ViewEmendaParlamentarLogRepository
  sqs:Sqs
  s3:S3


  
  
