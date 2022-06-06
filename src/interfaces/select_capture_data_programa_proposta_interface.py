from src.integration.sqs.sqs import Sqs
from src.integration.s3.s3 import S3
from src.repository.adapters.postgres.view_programa_proposta_log_repository import ViewProgramaPropostaLogRepository
from src.repository.adapters.postgres.view_programa_proposta_repository import ViewProgramaPropostaRepository

class SelectCaptureDataProgramaPropostaInterface:
  view_programa_proposta_repository:ViewProgramaPropostaRepository
  view_programa_proposta_log_repository:ViewProgramaPropostaLogRepository
  sqs:Sqs
  s3:S3


  
  
