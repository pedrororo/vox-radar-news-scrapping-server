import json

class SigarpCaptureDataProgramaQueueDTO:
  files_download:list

  def __init__(self, files_download:list):
    self.files_download = files_download

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)