from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_proposta_log_repository import ViewPropostaLogRepository
from src.repository.adapters.postgres.view_proposta_repository import ViewPropostaRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class SelectCaptureDataPropostaInterface:
  view_proposta_repository:ViewPropostaRepository
  view_proposta_log_repository:ViewPropostaLogRepository
  sqs:Sqs
  s3:S3


  
  
