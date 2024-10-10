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
from pages.article_page import ArticlePage

import sys
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

    def action_1(self):
        base_page = BasePage(self.driver, self.wait)
        base_page.go_to_page("https://www.facebook.com/MemesIns.Official/posts/pfbid033WU6qhsa4VMFTs7XfEGZqxhYmu2zYirBsoCsR34ySEVhD635kaUgYuT1zrvJKEm4l?_rdc=1&_rdr")
        base_page.close_dialog()
        # time.sleep(5)
        return base_page.get_oneof_a_elements()
    
    def action_2(self, href):
        base_page = BasePage(self.driver, self.wait)
        base_page.go_to_page(href)
        for attempt in range(3):
            try:
                # time.sleep(30)
                href = base_page.click_oneof_a_elements_portal()
            except Exception as e:
                print('Retrying to get a element')
                self.driver.switch_to.default_content()
                continue
            break
        return href
    
    def action_3(self, href):
        time.sleep(20)
        base_page = BasePage(self.driver, self.wait)
        base_page.go_to_page(href)
        base_page.click_oneof_links()
        
    def start_selenium(self, ads_id):
        
        # Replace with your actual API key and other parameters
        resp = requests.get(f"http://local.adspower.com:50325/api/v1/browser/start?user_id={ads_id}").json()
        print(resp)
        if resp["code"] != 0:
            print(resp["msg"])
            print("please check ads_id")
            sys.exit(1)
            
        chrome_driver = resp["data"]["webdriver"]
    
        options = webdriver.ChromeOptions()
    
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # # options.add_argument('--window-size=1920,1080')
        # options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        
        # if (len(session_id) > 0):
        #     options.add_argument(f"--user-data-dir=path_to_your_adspower_profile/{session_id}")  # Use the session ID
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        
        # Disable image loading
        prefs = {
            "profile.managed_default_content_settings.images": 2  # 2 means block images
        }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(service=ServiceChrome(executable_path=chrome_driver), options=options)
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.mp4", "*.webm", "*.ogg", "*.mov"]})

        self.wait = WebDriverWait(self.driver, 30)

    def close_selenium(self, ads_id):
        if self.driver:
            self.driver.quit()
            requests.get(f"http://local.adspower.com:50325/api/v1/browser/stop?user_id={ads_id}")
