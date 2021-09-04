
from django.core.mail import EmailMessage, send_mail
from booking.celery import app
import threading


# class EmailThread(threading.Thread):

#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)

#     def run(self):
#         self.email.send()


@app.task(name="Send email", serializer='json')
def send_email_to_user(data, **kwargs):
    # email = EmailMessage(
    #     subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
    # EmailThread(email).start()

    send_mail(subject=data['email_subject'], message=data['email_body'], from_email=None, recipient_list=[data['to_email']], **kwargs)


