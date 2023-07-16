from django.core.mail import send_mail as _send_email_django, EmailMultiAlternatives
from django.conf import settings
from celery import shared_task


@shared_task
def send_email_task(subject: str, message: str = '', email_receiver: list = []):
    """
        send email in background
    """
    email_from = settings.EMAIL_HOST_USER
    email_receiver = email_receiver or [settings.EMAIL_USER]
    _send_email_django(subject, message, email_from, email_receiver)


@shared_task
def send_email_html_task(subject: str, message: str = '', email_receiver: list = []):
    email_from = settings.EMAIL_HOST_USER
    email_receiver = email_receiver or [settings.EMAIL_USER]
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=email_from,
        to=email_receiver
    )
    email.attach_alternative(message, "text/html")
    email.send()