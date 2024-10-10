import pandas as pd
import logging
import time
import requests

from .ghost_logger import GhostLogger

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.article_page import ArticlePage

class BotManager:
    def __init__(self):
        self.logger = GhostLogger
        self.verbose = True
        # configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
        formatter = logging.Formatter(
            "\033[93m[INFO]\033[0m %(asctime)s \033[95m%(message)s\033[0m"
        )
        self.logger.handlers[0].setFormatter(formatter)

    def actions(self):
        base_page = BasePage(self.driver, self.wait)
        base_page.go_to_page("https://www.facebook.com/MemesIns.Official/posts/pfbid033WU6qhsa4VMFTs7XfEGZqxhYmu2zYirBsoCsR34ySEVhD635kaUgYuT1zrvJKEm4l?_rdc=1&_rdr")
        
        
        login_page = LoginPage(self.driver, self.wait)
        login_page.close_dialog()
        time.sleep(5)
        
        login_page.click_oneof_a_elements()
        time.sleep(30)
        
        login_page.click_oneof_a_elements_portal()
        
    # def vote_actions(self):
    #     base_page = BasePage(self.driver, self.wait)
    #     prev_link = ""
    #     count = 0
    #     success_list = []
    #     fail_list = []
    #     last_success = True
        
    #     s_time = time.time()
    #     for action in self.data:
    #         # if (count >= 5):
    #         #     break
    #         try:
    #             # Define the URL
    #             proxy_url = 'http://ma2proxy.dynalias.com:11911/3029597d60d4da043867b9b5480d35b6/reset?proxy=ma2proxy.dynalias.com:4002'

    #             # Make the GET request
    #             response = requests.get(proxy_url)

    #             # Check if the request was successful
    #             if response.status_code == 200:
    #                 data = response.json()  # Parse the JSON response
    #                 print(data)
    #             else:
    #                 print(f"Error proxy: {response.status_code} - {response.text}")
                    
    #             time.sleep(30)
                
    #             print(f"Username: {action["username"]}, Password: {action["pass"]} is logging ..... ")
                
    #             page_loading_s_time = time.time()
    #             if (prev_link != action["link"] or (not last_success)):
    #                 base_page.go_to_page(action["link"])
    #             prev_link = action["link"]
    #             print(f"1: {(time.time() - page_loading_s_time): .2f}s ")
                
    #             page_loading_s_time = time.time()
                
    #             login_page = LoginPage(self.driver, self.wait)
    #             login_page.login(action["username"], action["pass"])
                
    #             time.sleep(10)
                
    #             article_page = ArticlePage(self.driver, self.wait)
    #             if (action['upvote'] == 'yes'):
    #                 article_page.upvote()
    #             else:
    #                 article_page.downvote()
                    
    #             time.sleep(10)
    #             article_page.comment(action["comment"])
    #             time.sleep(10)
    #             login_page.logout()
    #             time.sleep(10)
                
    #             last_success = True
    #             success_list.append(action)
    #             print(f"2: {(time.time() - page_loading_s_time): .2f}s ")
                
    #         except Exception as e:
    #             self.logger.error(f"An error occurred: {e}")
    #             print(f"An error occurred: {e}")
    #             last_success = False
    #             fail_list.append(action)
                
    #         finally:
    #             count = count + 1
                
    #     print(f"Total Time: {(time.time() - s_time): .2f}s ")
                
    #     print(f"\nSuccess : {len(success_list)}, Fail : {len(fail_list)}")
    #     print(f"\nSuccess List\n{success_list}")
    #     print(f"\nFail List\n{fail_list}")
        
    def start_selenium(self):
        options = webdriver.ChromeOptions()
    
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # # options.add_argument('--window-size=1920,1080')
        # options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--disable-extensions")
        
        # Disable image loading
        prefs = {
            "profile.managed_default_content_settings.images": 2  # 2 means block images
        }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.mp4", "*.webm", "*.ogg", "*.mov"]})

        self.wait = WebDriverWait(self.driver, 30)

    def close_selenium(self):
        if self.driver:
            self.driver.quit()
