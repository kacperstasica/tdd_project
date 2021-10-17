from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
