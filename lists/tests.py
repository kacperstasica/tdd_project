from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_post_request(self):
        response = self.client.post(
            reverse('home'),
            data={'item_text': 'A new list item'}
        )
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
