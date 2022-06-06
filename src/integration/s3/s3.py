
import boto3
from ...config.envs import Envs

class S3:
  s3 = None

  def __init__(self):
    self.s3 = boto3.client(
      's3',
      aws_access_key_id=Envs.AWS['S3']['KEY'],
      aws_secret_access_key=Envs.AWS['S3']['SECRET']
    )

  def upload_file(self, file, bucket:str, name:str) -> bool:
    try:
      print(f'Save object s3 bucket:{bucket}, file:{name}')
      self.s3.put_object(Body=file, Bucket=bucket, Key=name)
    except Exception as err:
      print(err)
      raise

  def get_file(self, bucket:str, name:str):
    try:
      s3_object = self.s3.get_object(Bucket=bucket, Key=name)
      body = s3_object['Body']
      return body.read()
    except Exception as err:
      print(err)
      raise

  def get_all_files(self, bucket:str, folder:str):
    try:
      objects = self.s3.list_objects(Bucket=bucket, Prefix=folder)
      files = []
      for content in objects.get('Contents', []):
        if(content.get('Key') != folder):
          files.append(content.get('Key').replace(folder, ''))
      
      return files

    except Exception as err:
      print(err)
      raise

  def move_file(self, bucket:str, from_file:str, to_file:str):
    try:
      copy_source = {'Bucket': bucket, 'Key': from_file}
      print(bucket, from_file, to_file)
      s3_object = self.s3.copy_object(Bucket=bucket, CopySource=copy_source, Key=to_file)

      if(s3_object.get('ResponseMetadata').get('HTTPStatusCode') == 200):
        print(f'Delete file {from_file}')
        self.s3.delete_object(Bucket=bucket, Key=from_file)

      print(f'File moved from {from_file} to {to_file}')
    except Exception as err:
      print(err)
      raise