from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username_me(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть "me"'),
            params={'value': value},
        )


def validate_year(value):
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            'Этот год еще не начался')
