import json

class SigarpNotificationAddUserInDocumentQueueDTO:
  users_share_email:list[str]
  user_sender_name:str
  url_document:str
  description:str

  def __init__(self, users_share_email:list[str], user_sender_name:str, url_document:str, description:str):
    self.users_share_email = users_share_email
    self.user_sender_name = user_sender_name
    self.url_document = url_document
    self.description = description

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)