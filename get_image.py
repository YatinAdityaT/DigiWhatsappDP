import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Firefox(executable_path=r'D:\Installers\geckodriver.exe') # path to geckodriver for firefox

def click_on_element(x_path):
    element = driver.find_element_by_xpath(x_path)
    element.click()
    return element


WEBSITE            =  'https://www.oliverboorman.biz/projects/tools/digital_clock.php'

X_PATH_IMAGE       = f'//*[@id="canvas"]'
X_PATH_DIGITS      = f'//*[@id="ui-id-3"]'
X_PATH_WHITE       = f'/html/body/ul[1]/li[5]'
X_PATH_BLACK       = f'/html/body/ul[1]/li[2]'
X_PATH_BGCOLOR     = f'/html/body/main/section/fieldset[1]/label[2]/input'
X_PATH_HOURS       = f'/html/body/main/section/fieldset[3]/div[1]/label[1]/input'
X_PATH_MINUTES     = f'/html/body/main/section/fieldset[3]/div[1]/label[2]/input'
X_PATH_SECONDS     = f'/html/body/main/section/fieldset[3]/div[1]/label[3]/input'
X_PATH_TEXTCOLOR   = f'/html/body/main/section/fieldset[3]/div[2]/label[1]/input'
CSS_SELECTOR_AM_PM = f"div.column:nth-child(2) > label:nth-child(2) > select:nth-child(2)"

#open website
driver.get(WEBSITE)

# make background black
bgcolor = click_on_element(X_PATH_BGCOLOR)
_ = click_on_element(X_PATH_BLACK)

# click on time tab
time_ele = click_on_element(X_PATH_DIGITS)

#set 24hr format
am_pm_ele = Select(driver.find_element_by_css_selector(CSS_SELECTOR_AM_PM))
am_pm_ele.select_by_index(0)

#make text color white
textcolor = click_on_element(X_PATH_TEXTCOLOR)
_ = click_on_element(X_PATH_WHITE)

for hour in range(0,24,1):
	for minute in range(0,59,1):
		for second in range(0,59,10):
			# set hours
			hours_ele = click_on_element(X_PATH_HOURS)
			hours_ele.clear()
			hours_ele.send_keys(str(hour))

			#set minutes
			minutes_ele = click_on_element(X_PATH_MINUTES)
			minutes_ele.clear()
			minutes_ele.send_keys(str(minute))

			#set seconds
			seconds_ele = click_on_element(X_PATH_SECONDS)
			seconds_ele.clear()
			seconds_ele.send_keys(str(second))


			#save image
			with open('assets/{}_{}_{}.png'.format(str(hour),str(minute),str(second)), 'wb') as file:
			    file.write(driver.find_element_by_xpath(X_PATH_IMAGE).screenshot_as_png)
