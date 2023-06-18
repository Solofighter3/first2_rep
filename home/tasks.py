from celery import shared_task
from django.contrib.auth import get_user_model, settings
from django.core.mail import message, send_mail
@shared_task(bind=True)
def send_mails(self):
    users=get_user_model().objects.all()
    for user in users:
        mail_subject="hi"
        message="messaging to mail"
        to_email=user.email
        send_mail(subject=mail_subject,
                message=message,
                recipient_list=[to_email],
                fail_silently=True,
                from_email=settings.EMAIL_HOST_USER
                )
    return "done"

@shared_task(bind=True)
def send_mail1(self):
    users=get_user_model().objects.all()
    for user in users:
        mail_subject="Greetings"
        message="Happy new year sale is on now"
        to_email=user.email
        send_mail(subject=mail_subject,
                message=message,
                recipient_list=[to_email],
                fail_silently=True,
                from_email=settings.EMAIL_HOST_USER
                )
    return "done"
