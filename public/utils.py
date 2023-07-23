from django.conf import settings
from public import tasks


def log_write(log_obj, path=settings.LOG_CONFIG['path']):
    with open(path,'a+',encoding='utf-8') as file:
        file.write(log_obj.content)


def send_email(subject: str, message: str = '', email_receiver: list = []):
    tasks.send_email_task.delay(subject, message, email_receiver)


def send_email_html(subject: str, message: str = '', email_receiver: list = []):
    tasks.send_email_html_task.delay(subject, message, email_receiver)
