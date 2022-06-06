from abc import abstractmethod
from distutils.debug import DEBUG
from ...config.enum import Log
from ...utils.rollbar_wrapper import RollbarWrapper
from ...types.return_service import ReturnService
from ...interfaces.log_repository_interface import LogRepositoryInterface
from ...types.log_dto import LogDTO
from ...config.envs import Envs

import logging

class BaseService:
    log_repository: LogRepositoryInterface
    rollbar_wrapper: RollbarWrapper
    logger = None

    def __init__(self):
        self.rollbar_wrapper = RollbarWrapper()

        self.logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
  
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def exec(self, *args) -> ReturnService:
        pass

    def log(self, id:int, message:str, type: Log) -> ReturnService:
        self.logger.info(f'\n----- {message} -----\n')

        #if (type == Log.ERROR): 
            #self.rollbar_wrapper.error(message)

        log_dto: LogDTO = LogDTO(id, message)

        self.log_repository.add_log(log_dto)
