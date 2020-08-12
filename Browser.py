import random
import time

from selenium import webdriver


class Browser:
    _timeout = 30
    _min_input_time = 0.05
    _max_input_type = 0.2

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/accounts/login/")

    def type_in_input(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(self._min_input_time, self._max_input_type))

    def wait_for(self, seconds):
        ratio = seconds * 0.3
        time.sleep(random.uniform(seconds - ratio, seconds + ratio))
