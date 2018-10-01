from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('D:/Projects/JobTrackBoard/chromedriver.exe')

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Visitor enters a job-tack-board
        self.browser.get('http://localhost:8000')

        # Visitor sees a page title 'Job Track Board'
        self.assertIn('Job Track Board', self.browser.title)
        # The header mentions 'Jobs'
        header_text = self.browser.find_element_by_tag_name('h1').text # Selenium examines h1 tag
        self.assertIn('Jobs', header_text)

        # Visitor sees an option to add a job position
        inputbox = self.browser.find_element_by_id('id_new_job') # Selenium examines id="id_new_job"
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Add a new job position'
        )

        # A user adds 'Python Developer'
        inputbox.send_keys('Python Developer')  # Selenium types into input element

        # When a user hits enter the page updates, and now the page lists
        # "1: Python Developer" as an item in job positions lists
        inputbox.send_keys(Keys.ENTER) # Selenium presses Enter key
        time.sleep(1) # allow browser to reload before making more assertions

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr') # Selenium return several elements with tag 'tr'
        self.assertTrue(
            any(row.text == "Python Developer" for row in rows)
        )
    
        # other user stories

        
        self.fail("Add user stories and finish the test!")

if __name__ == '__main__':
    unittest.main(warnings='ignore')