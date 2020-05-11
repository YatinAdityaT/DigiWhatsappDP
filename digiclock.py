import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Firefox(executable_path=r'D:\Installers\geckodriver.exe')
driver.get('http://web.whatsapp.com')
response = input("Please confirm that you have scanned the barcode(type yes)")



def click_on_element(x_path):
    element = driver.find_element_by_xpath(x_path)
    element.click()
    return element


X_PATH_DP = f'/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img'
X_PATH_DP_EXPANDED = f'/html/body/div[1]/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img'
CSS_SELECTOR_DP_EXPANDED = '._2UkYn > span:nth-child(2)'
X_PATH_UPLOAD_PHOTO = f'/html/body/div[1]/div/span[4]/div/ul/li[3]/div'
CLASS_CHANGE_PICTURE = f'find_element_by_class_name'



if response == "yes":
	_ = click_on_element(X_PATH_DP)
	time.sleep(1)
	# dpx = driver.find_element_by_css_selector(CSS_SELECTOR_DP_EXPANDED)
	# dpx.click()

	#hover over the extended dp
	dp_hover_over = driver.find_element_by_class_name('_3FXB1')
	ActionChains(driver).move_to_element(dp_hover_over).perform() #.click(elementToClick).build()
	driver.find_element_by_class_name('WX_XW').click()
	driver.find_element_by_xpath('/html/body/div[1]/div/span[4]/div/ul/li[3]/div').send_keys(os.getcwd()+"/assets/0_0_0.png")
