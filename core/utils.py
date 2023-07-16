from . import tasks


def send_email(subject: str, message: str = '', email_receiver: list = []):
    tasks.send_email_task.delay(subject, message, email_receiver)


def send_email_html(subject: str, message: str = '', email_receiver: list = []):
    tasks.send_email_html_task.delay(subject, message, email_receiver)
