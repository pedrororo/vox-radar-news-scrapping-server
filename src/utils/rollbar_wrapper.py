import rollbar
from src.config.envs import Envs

class RollbarWrapper:

  def __init__(self):
    rollbar.init(Envs.ROLLBAR['KEY'], Envs.ENVIRONMENT)

  def error(self):
    rollbar.report_exc_info()
