import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GudlftHappyPath(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        # Navigate to the Flask application's home page
        self.driver.get('http://localhost:5000/')
        header = self.driver.find_element(By.TAG_NAME, "h1")
        time.sleep(2)
        # check home page displayed
        self.assertEqual(header.text,
                         'Welcome to the GUDLFT Registration Portal!')

        # navigate to clubs points board
        board_link = self.driver.find_element(By.LINK_TEXT, "view more")
        board_link.click()
        time.sleep(2)
        header = self.driver.find_element(By.TAG_NAME, "h2")
        # check board page displayed
        self.assertEqual(header.text, 'Clubs points board')

        # navigate back to home page
        board_link = self.driver.find_element(By.LINK_TEXT,
                                              "back to login page")
        board_link.click()

        time.sleep(2)
        # login
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("johny@amstrength.co")
        time.sleep(2)
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        # check welcome page displayed for correct user
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Welcome, johny@amstrength.co')

        time.sleep(2)
        # click on the fourth competition booking link
        booking_link_list = self.driver.find_elements(By.LINK_TEXT,
                                                      "Book Places")
        competition_booking = booking_link_list[3]
        competition_booking.click()
        # check correct competition displayed
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Holiday Havoc')

        time.sleep(2)
        # book two places
        places_input = self.driver.find_element(By.NAME, "places")
        places_input.send_keys("2")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        # the submit button is the second on page
        time.sleep(2)
        submit_places_button = buttons[1]
        submit_places_button.click()
        time.sleep(2)
        # check booking message succesful display
        success_message = self.driver.find_element(By.CLASS_NAME,
                                                   "alert")
        self.assertEqual(success_message.text, "Great-booking complete!")


if __name__ == '__main__':
    unittest.main()
