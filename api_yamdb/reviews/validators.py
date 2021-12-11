from datetime import datetime

from django.core.exceptions import ValidationError


def validate_username_me(value):
    if value == 'me':
        raise ValidationError(
            ('Имя пользователя не может быть "me"'),
            params={'value': value},
        )


def validate_year(value):
    now = datetime.now().year
    if value > now:
        raise ValidationError(
            'Этот год еще не начался')
