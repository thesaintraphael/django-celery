from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings


@shared_task
def send_mail():
    email = 'raphasalimov@gmail.com'
    email_subject = 'Testing email automation'
    email_body = 'Hello, Rafael. We testing dat shit'

    new_email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email]
    )

    return new_email.send(fail_silently=False)
