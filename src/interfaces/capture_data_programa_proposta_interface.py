from abc import abstractmethod
import json
from src.types.log_dto import LogDTO
from src.repository.adapters.postgres.view_programa_proposta_log_repository import ViewProgramaPropostaLogRepository
from src.repository.adapters.postgres.view_programa_proposta_repository import ViewProgramaPropostaRepository
from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3

class CaptureDataProgramaPropostaInterface:
  view_programa_proposta_repository:ViewProgramaPropostaRepository
  view_programa_proposta_log_repository:ViewProgramaPropostaLogRepository
  sqs:Sqs
  s3:S3


  
  
