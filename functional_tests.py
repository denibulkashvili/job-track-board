from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('D:/Projects/JobTrackBoard/chromedriver.exe')

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Visitor enters a job-tack-board
        self.browser.get('http://localhost:8000')

        # Visitor sees a page title and header mention job-track-board
        self.assertIn('JobTrackBoard', self.browser.title)
        self.fail('Finish the test!')

        # Visitor sees an option to add a job position
        # other user stories

if __name__ == '__main__':
    unittest.main(warnings='ignore')