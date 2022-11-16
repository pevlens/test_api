from django.core.mail import send_mail
from django.conf import settings
import datetime
import django
django.setup()
from .models import TransactionsUser
from django.contrib.auth.models import User


def send_spam():
   
    subject = f'Отчет за { datetime.datetime.now}'

    for email in User.objects.all():
        message = f"Вы потратили за все время {sum([i.summ for i in TransactionsUser.objects.filter(person = email.pk)])}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email.email]
        send_mail( subject, message, email_from, recipient_list, fail_silently=False)
    pass