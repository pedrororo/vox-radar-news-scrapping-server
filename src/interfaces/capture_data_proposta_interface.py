from abc import abstractmethod
import json
from src.repository.adapters.postgres.view_proposta_log_repository import ViewPropostaLogRepository
from src.repository.adapters.postgres.view_proposta_repository import ViewPropostaRepository
from src.integration.sqs.sqs import Sqs

class CaptureDataPropostaInterface:
  view_proposta_repository:ViewPropostaRepository
  view_proposta_log_repository:ViewPropostaLogRepository
  sqs:Sqs


  
  
