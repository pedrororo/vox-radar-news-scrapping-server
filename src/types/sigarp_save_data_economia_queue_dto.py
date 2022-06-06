import json

class SigarpSaveDataEconomiaQueueDTO:
  files_download:list
  type: str

  def __init__(self, files_download:list, type:str):
    self.files_download = files_download
    self.type = type

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)