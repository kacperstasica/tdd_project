from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
