from clr.models import Data
from selenium import webdriver
from django.conf import settings

# driver = webdriver.Chrome(settings.BASE_DIR + 'chromedriver')
# driver.implicitly_wait(3)

class Crawller:
    def start(self):
        driver = webdriver.Chrome(settings.BASE_DIR + 'chromedriver')
        driver.implicitly_wait(3)
        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("abcd")
        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()