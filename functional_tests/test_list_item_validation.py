from selenium.webdriver.common.keys import Keys
from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):
        # user tries to enter an empty list item

        # the home page refreshes and there is a message that lists items cannot be blank

        # user tries again with some text and it works

        # user tries to add another blank item

        # user receives similar warning on a list page

        # user can correct it with filling some text in

        self.fail('write me')
