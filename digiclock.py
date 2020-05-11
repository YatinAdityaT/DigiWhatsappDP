import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Firefox(executable_path=r'D:\Installers\geckodriver.exe')
driver.get('https://www.oliverboorman.biz/projects/tools/digital_clock.php')

#//*[@id="ui-id-3"]

def click_on_element(x_path):
    element = driver.find_element_by_xpath(x_path)
    element.click()
    return element


CSS_SELECTOR_OF_BGCOLOR = f'#tab-1 > label:nth-child(2) > input:nth-child(2)'
X_PATH_BGCOLOR = f'/html/body/main/section/fieldset[1]/label[2]/input'
# bgcolor = driver.find_element_by_css_selector(CSS_SELECTOR_OF_BGCOLOR)
bgcolor = click_on_element(X_PATH_BGCOLOR)
CLASS_NAME_FOR_COLOR_SELECTION = 'basicColourSelector'
bgcolor.select_by_visible_text('black')

X_PATH_TIME = f'//*[@id="ui-id-3"]'
time_ele = click_on_element(X_PATH_TIME)

X_PATH_HOURS = '/html/body/main/section/fieldset[3]/div[1]/label[1]/input'
hours_ele = click_on_element(X_PATH_HOURS)
hours_ele.clear()
hours_ele.send_keys('00')

X_PATH_MINUTES = '/html/body/main/section/fieldset[3]/div[1]/label[2]/input'
minutes_ele = click_on_element(X_PATH_MINUTES)
minutes_ele.clear()
minutes_ele.send_keys('00')

X_PATH_SECONDS = '/html/body/main/section/fieldset[3]/div[1]/label[3]/input'
seconds_ele = click_on_element(X_PATH_SECONDS)
seconds_ele.clear()
seconds_ele.send_keys('00')

# AM_PM = '/html/body/main/section/fieldset[3]/div[2]/label[2]/select'
am_pm_ele = Select(driver.find_element_by_css_selector("div.column:nth-child(2) > label:nth-child(2) > select:nth-child(2)"))
am_pm_ele.select_by_index(0)

X_PATH_IMAGE = '//*[@id="canvas"]'


with open('test.png', 'wb') as file:
    file.write(driver.find_element_by_xpath(X_PATH_IMAGE).screenshot_as_png)
