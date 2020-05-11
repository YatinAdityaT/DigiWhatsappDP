import os
import time
import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


X_PATH_DP = f'/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img'
X_PATH_DP2 = f'/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/div/span'
CSS_SELECTOR_DP_EXPANDED = '._2UkYn > span:nth-child(2)'
X_PATH_UPLOAD_PHOTO = f'/html/body/div[1]/div/span[4]/div/ul/li[3]/div'
CLASS_CHANGE_PICTURE = f'find_element_by_class_name'
X_PATH_TICKMARK = f'/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span'


def click_on_element(x_path):
    element = driver.find_element_by_xpath(x_path)
    element.click()
    return element

#hover over the extended dp and then click
def hover_and_click_on_upload():

	# refresh the page
	driver.refresh()
	time.sleep(10)

	# try clicking on dp
	try:
		_ = click_on_element(X_PATH_DP)
	except NoSuchElementException:
		_ = click_on_element(X_PATH_DP2)

	print('clicked on dp')


	#hover over extended dp to show WX_XW class
	dp_hover_over = driver.find_element_by_class_name('_3FXB1')
	ActionChains(driver).move_to_element(dp_hover_over).perform() 
	print('hover executed')

	time.sleep(0.5)

	# try to get WX_XW class
	while True:
		try:
			driver.find_element_by_class_name('WX_XW').click()
			break
		except:
			dp_hover_over = driver.find_element_by_class_name('_3FXB1')
			print('dp_hover_over found!')
			ActionChains(driver).move_to_element(dp_hover_over).perform() 

	print('click executed')

	#short time delay to let elements in drop-down box to appear
	time.sleep(0.5)

	try:
		element = driver.find_element_by_css_selector('li._3L0q3:nth-child(3) > div:nth-child(1)')
	except NoSuchElementException:
		element = driver.find_element_by_css_selector('li._3L0q3:nth-child(2) > div:nth-child(1)')

	element.click()
	print('clicked on upload')


def main():

	hover_and_click_on_upload()

	prev_minute = None

	while True:

		now    = datetime.datetime.now()
		hour   = now.hour
		minute = now.minute

		if hour < 12 :
			meridiem = 'am'
		else:
			meridiem = 'pm'
			hour = hour - 12

		# _ is used to avoid the code from running many times when minute meets the criteria
		if prev_minute != minute:
			prev_minute = minute

			#get the required image path from hour,min and second
			image_path = '{}_{}_{}.png'.format(hour,minute,meridiem)
			print('uploading :',image_path)

			#pyautogui automatically writes the path into the file explorer and presses enter
			PATH = os.path.join(os.getcwd(),os.path.relpath('assets/reshaped/'+image_path))
			pyautogui.write(PATH) 
			time.sleep(0.5)
			pyautogui.press('return')
			pyautogui.press('return')



			#once the image is selected, give it a second to show up and then click the tick mark
			time.sleep(1)
			__ = click_on_element(X_PATH_TICKMARK)

			# Your image is now uploaded! repeat! :-)
			time.sleep(10)
			hover_and_click_on_upload()


if __name__ == "__main__":

	print('Prepare your phone to scan the barcode... QUICK!!!')
	time.sleep(5)
	driver = webdriver.Firefox(executable_path=r'D:\Installers\geckodriver.exe')
	driver.get('http://web.whatsapp.com')
	print("Scan the barcode.. you have 5 seconds")
	time.sleep(10) 

	main()