from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By

from functional_tests.base import FunctionalTest


User = get_user_model()


class MyListsTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # kacper is a logged in user
        self.create_pre_authenticated_session('kacper@example.com')

        # kacper goes to home page and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item('Immanentize eschaton')
        self.add_list_item('Reticulate splines')
        first_list_url = self.browser.current_url

        # he notices "my list" link, for the first time
        self.browser.find_element(By.LINK_TEXT, 'My Lists').click()

        # he sees that his list is there, named according
        # to first list item
        self.wait_for(
            lambda: self.browser.find_element(By.LINK_TEXT, 'Immanentize eschaton')
        )
        self.browser.find_element(By.LINK_TEXT, 'Immanentize eschaton').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # he decides to start another list just to see
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # under "my list" his new list appears
        self.browser.find_element(By.LINK_TEXT, 'My Lists').click()
        self.wait_for(
            lambda: self.browser.find_element(By.LINK_TEXT, 'Click cows')
        )
        self.browser.find_element(By.LINK_TEXT, 'Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )
        # he logs out. "my lists" option disappears
        self.browser.find_element(By.LINK_TEXT, 'Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements(By.LINK_TEXT, 'My Lists'),
            []
        ))
