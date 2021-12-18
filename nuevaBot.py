from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("window-size=1400,600")
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options = chrome_options)


Email = "***"
Password = "***"


def NuevaLogin():
	driver.get('https://my.nuevaschool.org/login.php?targeturl=UHRVQnd5cTVQNzVCYlBlaUxNdGdNdz09')
	print('Reached Website')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/input[1]').send_keys(Email)
	print('Input Username')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/input[2]').send_keys(Password)
	print('Input Password')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/button[1]').click()
	print('Logged In')
	time.sleep(2)
	# driver.find_element_by_xpath('/html/body/div/div/div[3]/button').click()
	# print('popup')
	# time.sleep(2)
def COVIDForm():
	driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[1]/ul/div[1]/span/button').click()
	print('Opened form')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[1]/p[3]/label[2]/input').click()
	print('First Question')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/p[2]/label[2]/input').click()
	print('Second Question')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[3]/p[2]/label[2]/input').click()
	print('Third Question')
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
	print('Submitted')

while True:
	time.sleep(30)
	current_time = time.localtime(time.time())
	if current_time.tm_hour == 14 and current_time.tm_min == 0:
		NuevaLogin()
		COVIDForm()
