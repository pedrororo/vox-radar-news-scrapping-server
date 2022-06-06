
import boto3
from src.domain.base.base_service import BaseService

from src.integration.sqs.my_listener_queue import MyListenerQueue
from src.integration.sqs.queue_processors import QueueProcessors
from src.types.return_service import ReturnService
from ...config.envs import Envs
from typing import List
from logzero import logger
from botocore.exceptions import ClientError

class Sqs:
  client = None
  resource = None

  def __init__(self):
    print(Envs.AWS['SQS']['REGION'])
    self.client = boto3.client(
      'sqs',
      aws_access_key_id=Envs.AWS['SQS']['KEY'],
      aws_secret_access_key=Envs.AWS['SQS']['SECRET'],
      region_name=Envs.AWS['SQS']['REGION']
    )

    self.resource = boto3.resource(
      'sqs',
      aws_access_key_id=Envs.AWS['SQS']['KEY'],
      aws_secret_access_key=Envs.AWS['SQS']['SECRET'],
      region_name=Envs.AWS['SQS']['REGION']
    )

  def send_message_queue(self, name_queue:str, message:str, delay_seconds:int = 0) -> bool:
    try:
      queue_url:str = f"https://sqs.{Envs.AWS['SQS']['REGION']}.amazonaws.com/{Envs.AWS['ACCOUNT_ID']}/{name_queue}"
      response = self.client.send_message(QueueUrl=queue_url, MessageBody=message, DelaySeconds=delay_seconds)

      if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(f"\n----- Message send to {name_queue} success -----\n")
        print(f"\n----- Body {message} -----\n")
        return True
      else:
        print(f"\n----- Message send to ${name_queue} error -----\n")
        print(f"\n----- Body {message} -----\n")
        return False
    except Exception as err:
      print(err)
      raise
  
  # def receive_message_queues(self, queue_processors: List[QueueProcessors]):

  #   # my_event_bus = EventBus()
  #   # EventBus.register_buses([my_event_bus])

  #   my_queue = []
    
  #   for queue_processor in queue_processors:
  #     logger.info(f"Add queue {queue_processor.queue_name}")
  #     my_queue.append(QueueConfig(self.resource, queue_processor.queue_name, queue_processor.processor, self.my_event_bus, queue_type='long-poll', region_name=Envs.AWS['SQS']['REGION']) )

  #   my_listener = MyListenerQueue(my_queue)
  #   my_listener.listen()

  def receive_message_queues(self, queue_url:str, queue_processors: BaseService):
    print(f"Add queue {queue_url}")

    queue = self.resource.get_queue_by_name(QueueName=queue_url)

    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1, WaitTimeSeconds=5)
        print('Amount of existing Queue messages', len(messages))
        for message in messages:
          print('msg:',message.body)
          try:
            result_queue:ReturnService = queue_processors().exec(message.body)
            #if result_queue.status:
            message.delete()

          except Exception:
            print('Error:', Exception.__str__())



