
from smtplib import SMTP 
from src.config.envs import Envs
from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from src.integration.smtp.smtp_base import SMTPBase

class Email(SMTPBase):
  env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))

  def send_add_user_in_document_template(self, subject:str, to_email:list[str], **kwargs) -> bool:
    try:

      template = self.env.get_template('add_user_in_document.html')
      body_content = template.render(**kwargs)

      self.send_email(subject, to_email, body_content)

    except Exception as err:
      print(err)
      raise

  