import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test!') - great thing to remember!
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # entering to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # typing into a text box of to do list
        input_box.send_keys('Buy peacock feathers')
        # hitting enter and having 'Buy peacock feathers' on a list of to-dos
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        self.fail('Finish the test!')


# checks if it is runned from the command line rather than just imported by another script
if __name__ == '__main__':
    # automatically runs unittest test runner, which finds tests, methods and classes in the
    # file and runs them
    unittest.main()
