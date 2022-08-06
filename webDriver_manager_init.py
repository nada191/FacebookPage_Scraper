from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def install_webDriver_manager():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Safari()
    # return driver
