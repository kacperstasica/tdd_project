from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import FunctionalTest


def quit_if_possible(browser):
    try: browser.quit()
    except: pass


class SharingTest(FunctionalTest):

    def test_can_share_a_list_with_another_user(self):
        # kacper is a logged in user
        self.create_pre_authenticated_session('kacper@example.com')
        kacper_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(kacper_browser))

        # his friend Onificerous is also hanging on the lists side
        oni_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(oni_browser))
        self.browser = oni_browser
        self.create_pre_authenticated_session('oni@example.com')

        # kacper goes to home page and creates a list
        self.browser = kacper_browser
        self.browser.get(self.live_server_url)
        self.add_list_item('Get help')

        # he notices 'Share this list' option
        share_box = self.browser.find_element(By.CSS_SELECTOR, 'input[name="sharee"]')
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
