import random
import sys
import time
import yaml

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Browser import Browser

class Instagram:
    _general_timeout = 30
    _elements_timeout = 10
    _likes = 0
    _hashtag_likes = 0
    _visited_photos = {""}
    _hashtag_like_limit = 0

    def __init__(self):
        self.browser = Browser()
        WebDriverWait(self.browser.driver, self._general_timeout).until(
            EC.presence_of_element_located((By.NAME, "username")))
