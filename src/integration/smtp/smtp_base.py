
from smtplib import SMTP 
from src.config.envs import Envs
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class SMTPBase:

  def send_email(self, subject:str, to_email:list[str], body_content) -> bool:
    try:
      smtp = SMTP(Envs.SMTP[0]['HOST'], Envs.SMTP[0]['PORT'])
      smtp.starttls()
      smtp.login(Envs.SMTP[0]['USER'], Envs.SMTP[0]['PASSWORD'])

      email = ','.join(to_email)

      message = MIMEMultipart()
      message['Subject'] = subject
      message['From'] = Envs.SMTP[0]['FROM']
      message['To'] = email

      message.attach(MIMEText(body_content, "html"))
      msgBody = message.as_string()
      
      smtp.sendmail(Envs.SMTP[0]['FROM'], email, msgBody)

      print(f'----- sending email to {email} -----')
      
    except Exception as err:
      print(err)
      raise
    finally:
      if smtp:
        smtp.quit()

  