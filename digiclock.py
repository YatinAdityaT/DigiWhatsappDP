import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Firefox(executable_path=r'D:\Installers\geckodriver.exe')
driver.get('https://www.oliverboorman.biz/projects/tools/digital_clock.php')
