from selenium import webdriver
from selenium.webdriver.common.by import By

from .base import FunctionalTest
from .list_page import ListPage
from .my_lists_page import MyListPage


def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass


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
        list_page = ListPage(self).add_list_item('Get help')

        # he notices 'Share this list' option
        share_box = list_page.get_share_box()
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friends@email.com'
        )

        # he shares the list with
        # the page updates to say that it's shared with Onificerous
        list_page.share_list_with('oni@example.com')

        # Onificerous goes to the list page with his browser
        self.browser = oni_browser
        MyListPage(self).go_to_my_lists_page()

        # he sees kacper's list page there
        self.browser.find_element(By.LINK_TEXT, 'Get help').click()

        # on a list page, Onificerous sees that its kacpers list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'kacper@example.com'
        ))

        # he adds an item to the list
        list_page.add_list_item('Hi Kacper!')

        # when kacper refreshes the page, he sees Oni addition
        self.browser = kacper_browser
        self.browser.refresh()
        list_page.wait_for_row_in_list_table('Hi Kacper!', 2)
