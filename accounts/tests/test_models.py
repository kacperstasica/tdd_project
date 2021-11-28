from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Token

User = get_user_model()


class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email='a@b.pl')
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User(email='a@wp.pl')
        self.assertEqual(user.pk, 'a@wp.pl')


class TokenModelTest(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='a@b.pl')
        token2 = Token.objects.create(email='a@b.pl')
        self.assertNotEqual(token1.uid, token2.uid)
