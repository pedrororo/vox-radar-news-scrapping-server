from typing import List
from importlib_metadata import os
from logzero import logger

from src.utils.utils import Utils
from ..integration.sqs.sqs import Sqs
from ..config.envs import Envs
from ..domain.capture_data_cidadania_scrapping_service import CaptureDataCidadaniaScrappingService

class QueuesApp():
    sqs:Sqs

    def __init__(self):
        self.sqs = Sqs()
    
    def create_app(self, queue:str):
        logger.info(f"Create app to queues on {Envs.ENVIRONMENT[0]}")
        
        queue_selected = queue + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
        
        if queue_selected.upper() == Envs.AWS['SQS']['QUEUE']['SIGARP_CIDADANIA_SCRAPPING']:
            self.sqs.receive_message_queues(Envs.AWS['SQS']['QUEUE']['SIGARP_CIDADANIA_SCRAPPING'], CaptureDataCidadaniaScrappingService)
        else:
            print('No queue selected')


