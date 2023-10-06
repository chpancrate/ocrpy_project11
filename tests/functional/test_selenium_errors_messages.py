import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GudlftErrorsMessages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        # Navigate to the Flask application's home page
        self.driver.get('http://localhost:5000/')
        time.sleep(2)
        # check home page displayed
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text,
                         'Welcome to the GUDLFT Registration Portal!')

        # login with wrong email
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("wrong@email.com")
        time.sleep(2)
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        # check home page still displayed
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text,
                         'Welcome to the GUDLFT Registration Portal!')
        # check the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME,
                                                 "alert")
        self.assertEqual(error_message.text, "Unknown email")

        # log with a correct email
        # user points = 11
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("ness@clanshred.com.au")
        time.sleep(2)
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        # check welcome page displayed for correct user
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Welcome, ness@clanshred.com.au')

        # click on the eigth competition booking link
        # places = 7
        booking_link_list = self.driver.find_elements(By.LINK_TEXT,
                                                      "Book Places")
        competition_booking = booking_link_list[7]
        competition_booking.click()
        time.sleep(2)
        # check correct competition displayed
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Fall Classic')

        # book 12 places > 11 points available
        places_input = self.driver.find_element(By.NAME, "places")
        places_input.send_keys("12")
        time.sleep(2)
        # the submit button is the second on page
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        submit_places_button = buttons[1]
        submit_places_button.click()
        time.sleep(2)
        # check the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME,
                                                 "alert")
        self.assertEqual(error_message.text, "You do not have enough points.")

        # book 8 places > 7 places in competition
        places_input = self.driver.find_element(By.NAME, "places")
        places_input.send_keys("8")
        time.sleep(2)
        # the submit button is the second on page
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        submit_places_button = buttons[1]
        submit_places_button.click()
        time.sleep(2)
        # check the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME,
                                                 "alert")
        self.assertEqual(error_message.text,
                         "There is not enough places in the competition.")

        # click on back to list link
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        # the return to list link is the 1st button on page
        submit_places_button = buttons[0]
        submit_places_button.click()
        time.sleep(2)
        # check back on welcome page
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Welcome, ness@clanshred.com.au')

        # click on log out
        logout_link = self.driver.find_element(By.LINK_TEXT,
                                               "Logout")
        logout_link.click()
        time.sleep(2)
        # check home page displayed
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text,
                         'Welcome to the GUDLFT Registration Portal!')

        # log with another correct email
        # user points = 18
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("bearslifting@omail.com")
        time.sleep(2)
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        # check welcome page displayed for correct user
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Welcome, bearslifting@omail.com')

        # click on the first competition booking link
        # places = 35
        booking_link_list = self.driver.find_elements(By.LINK_TEXT,
                                                      "Book Places")
        competition_booking = booking_link_list[0]
        competition_booking.click()
        time.sleep(2)
        # check correct competition displayed
        header = self.driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(header.text, 'Tacoma Rookie Competition')

        # book 13 places > 12 places in competition
        places_input = self.driver.find_element(By.NAME, "places")
        places_input.send_keys("13")
        time.sleep(2)
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        # the submit button is the second on page
        submit_places_button = buttons[1]
        submit_places_button.click()
        time.sleep(2)
        # check the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME,
                                                 "alert")
        self.assertEqual(error_message.text,
                         "You cannot book more than 12 places.")


if __name__ == '__main__':
    unittest.main()
