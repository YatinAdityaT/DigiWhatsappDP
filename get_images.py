import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

SAVE_PATH          = f'assets/downloaded_images/'
EXECUTABLE_PATH    = r'D:\Installers\geckodriver.exe' # path to geckodriver for firefox
WEBSITE            = f'https://www.oliverboorman.biz/projects/tools/digital_clock.php'
X_PATH_IMAGE       = f'//*[@id="canvas"]'
X_PATH_DIGITS      = f'//*[@id="ui-id-3"]'
X_PATH_WHITE       = f'/html/body/ul[1]/li[5]'
X_PATH_BLACK       = f'/html/body/ul[1]/li[2]'
X_PATH_BGCOLOR     = f'/html/body/main/section/fieldset[1]/label[2]/input'
X_PATH_HOURS       = f'/html/body/main/section/fieldset[3]/div[1]/label[1]/input'
X_PATH_MINUTES     = f'/html/body/main/section/fieldset[3]/div[1]/label[2]/input'
X_PATH_SECONDS     = f'/html/body/main/section/fieldset[3]/div[1]/label[3]/input'
X_PATH_CHECKBOX    = f'/html/body/main/section/fieldset[3]/div[1]/label[4]/input'
X_PATH_TEXTCOLOR   = f'/html/body/main/section/fieldset[3]/div[2]/label[1]/input'
CSS_SELECTOR_AM_PM = f"div.column:nth-child(2) > label:nth-child(2) > select:nth-child(2)"

def click_on_element(x_path):
    element = driver.find_element_by_xpath(x_path)
    element.click()
    return element


def save_minutes(hour,meridiem):
	for minute in range(0,60):
		for second in range(0,2): #this is a workaround I had to use to get the saved images to have a change in the minutes... 
								  #seconds won't actully be displayed
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
				seconds_ele.send_keys(second)

				if not os.path.exists(SAVE_PATH):
					os.mkdir(SAVE_PATH)

				#save image
				with open(os.path.join(SAVE_PATH,'{}_{}_{}.png'.format(str(hour),str(minute),meridiem)), 'wb') as file:
				    file.write(driver.find_element_by_xpath(X_PATH_IMAGE).screenshot_as_png)

def main():
	#make background black
	bgcolor = click_on_element(X_PATH_BGCOLOR)
	_ = click_on_element(X_PATH_BLACK)

	#click on time tab
	time_ele = click_on_element(X_PATH_DIGITS)

	#disable seconds
	_ = click_on_element(X_PATH_CHECKBOX)
	# driver.find_element_by_css_selector(CSS_SELECTOR_AM_PM)

	#make text color white
	textcolor = click_on_element(X_PATH_TEXTCOLOR)
	_ = click_on_element(X_PATH_WHITE)
	# 'div.column:nth-child(1) > label:nth-child(4) > input:nth-child(2)'

	for meridiem_index,meridiem in enumerate(['am','pm']): # will give 0 and then 1
		#set am or pm
		am_pm_ele = Select(driver.find_element_by_css_selector(CSS_SELECTOR_AM_PM))
		am_pm_ele.select_by_index(meridiem_index+1)

		for hour in range(1,13):
			save_minutes(hour,meridiem)

if __name__ == "__main__":
	driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH) 
	driver.get(WEBSITE) #open website
	main()
