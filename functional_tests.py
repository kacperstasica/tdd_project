from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


# checks if it is runned from the command line rather than just imported by another script
if __name__ == '__main__':
    # automatically runs unittest test runner, which finds tests, methods and classes in the
    # file and runs them
    unittest.main()
