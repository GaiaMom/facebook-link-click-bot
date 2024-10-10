from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import LoginPageLocators
import time
import random
import urllib.parse

class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.locator = LoginPageLocators
        super().__init__(driver, wait)

    def close_dialog(self):
        # Wait for the page to load and for the dialog to appear
        self.wait.until(
            EC.presence_of_element_located(self.locator.DIALOG_CONTAINER)
        )

        # Locate the dialog element
        dialog_element = self.driver.find_element(By.CSS_SELECTOR, 'div[role="dialog"]')

        # Get the first <div> child of the dialog
        first_child_div = dialog_element.find_element(By.XPATH, './div[1]')
        
        # Wait for the first child <div> to be clickable
        self.wait.until(
            EC.element_to_be_clickable(first_child_div)
        )

        # Click the first child <div>
        first_child_div.click()
    
    def click_oneof_a_elements(self):
        # Wait for the page to load and locate <a> elements
        self.wait.until(
            EC.presence_of_all_elements_located(self.locator.A_ELEMENT)
        )

        # Get a list of all <a> elements
        links = self.driver.find_elements(By.CSS_SELECTOR, 'a[rel="nofollow noreferrer"]')

        # Check if there are any links found
        if links:
            # Select a random link
            random_link = random.choice(links)

            # Wait for the link to be clickable
            self.wait.until(
                EC.element_to_be_clickable(random_link)
            )

            href = random_link.get_attribute('href')

            # Check if the href contains a parameter `u`
            parsed_url = urllib.parse.urlparse(href)
            query_params = urllib.parse.parse_qs(parsed_url.query)

            # Decode the URL if `u` parameter exists
            if 'u' in query_params:
                # The `u` parameter may contain multiple values, we take the first one
                encoded_url = query_params['u'][0]
                decoded_url = urllib.parse.unquote(encoded_url)
                print(f"Decoded URL: {decoded_url}")
                
                # Navigate to the decoded URL
                self.driver.get(decoded_url)
            else:
                # Navigate to the href location
                self.driver.get(href)
                print(f"Navigated to: {href}")
            
    def click_oneof_a_elements_portal(self):
        
        # Wait for the iframe to be present and switch to it
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
        )
        
        # Switch to the first iframe found
        iframe = self.driver.find_element(By.TAG_NAME, 'iframe')
        self.driver.switch_to.frame(iframe)

        # Wait for <a> elements with data-role="0" to be present
        self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-role="0"]'))
        )

        # Get a list of all <a> elements with data-role="0"
        links = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-role="0"]')

        # Check if there are any links found
        if links:
            # Select a random link
            random_link = random.choice(links)

            # Get the href attribute of the selected link
            href = random_link.get_attribute('href')

            # Print the href value
            print(f"Selected link href: {href}")

            # Navigate to the href
            self.driver.get(href)
        else:
            print("No links with data-role='0' found in the iframe.")

