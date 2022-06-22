import random
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


def generate_confirmation_code():
    return int(''.join([str(random.randint(0, 10)) for _ in range(6)]))


def send_verification_mail(email: str, confirmation_code: int):
    subject = 'YaMDB confirmation code'
    message = f'Your confirmation code:\n{confirmation_code}\nThanks for using YaMDB.'
    from_email = 'support@yamdb.ru'
    recipient_list = [email, ]
    send_mail(subject, message, from_email, recipient_list)


def get_token_for_user(user: User):
    refresh = RefreshToken.for_user(user)
    return {
        'token': str(refresh.access_token)
    }