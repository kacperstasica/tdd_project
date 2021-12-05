from django.contrib.auth.backends import BaseBackend

from accounts.models import Token, User


class PasswordlessAuthenticationBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        try:
            my_token = Token.objects.get(uid=kwargs.get('uid'))
            return User.objects.get(email=my_token.email)
        except User.DoesNotExist:
            return User.objects.create(email=my_token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
