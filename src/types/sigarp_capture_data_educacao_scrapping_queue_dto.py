import json

class SigarpCaptureDataEducacaoScrappingQueueDTO:
  state:str
  city:str

  def __init__(self, state:str, city:str):
    self.state = state
    self.city = city

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)