from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

port = random.randint(1111,9999)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=" + str(port))
chrome_options.add_argument("window-size=1400,600")
chrome_options.add_argument("headless")

# driver = webdriver.Chrome(options = chrome_options)
driver = webdriver.Chrome("/Users/danielappenzeller/dev/coding/webtest/chromedriver", options = chrome_options)
print("localhost:" + str(port))

Email = "dappenzeller26@csus.org"
Password = "TtqU320*"

def GoogleLogin(url, usernameID, username, loginbutton1, passwordId, password, loginbutton2):
	driver.get(url)
	delay = time.time() + 5
	while True: 
		if driver.find_elements_by_xpath(usernameID):
			driver.find_element_by_xpath(usernameID).send_keys(username)
			break
		if delay <= time.time():
			break
	delay = time.time() + 5
	while True: 
		if driver.find_elements_by_xpath(loginbutton1):
			driver.find_element_by_xpath(loginbutton1).click()
			time.sleep(2)
			break
		if delay <= time.time():
			break
	delay = time.time() + 5
	while True: 
		if driver.find_elements_by_xpath(passwordId):
			time.sleep(.5)
			driver.find_element_by_xpath(passwordId).send_keys(password)
			break
		if delay <= time.time():
			break				
	delay = time.time() + 5
	while True: 
		if driver.find_elements_by_xpath(loginbutton2):
			driver.find_element_by_xpath(loginbutton2).click()
			time.sleep(10)
			break
		if delay <= time.time():
			break
def GmailNav(search, email2, link):
	time.sleep(5)
	driver.find_element_by_xpath(search).send_keys("bpollock@csus.org")
	print("search")
	time.sleep(1)
	driver.find_element_by_xpath(search).send_keys(Keys.RETURN)
	print("return")
	time.sleep(5)
	driver.find_element_by_xpath(email2).send_keys(Keys.RETURN)
	print("email")
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	print("scroll")
	time.sleep(3)
	link = driver.find_element_by_xpath(link).get_attribute("href")
	print(link)
	driver.get(link)
def RuvnaForm(form, first, second, third, submit):
	time.sleep(5)
	driver.find_element_by_xpath(form).click()
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)
	driver.find_element_by_xpath(first).click()
	time.sleep(3)
	driver.find_element_by_xpath(second).click()
	time.sleep(3)
	driver.find_element_by_xpath(third).click()
	time.sleep(3)
	driver.find_element_by_xpath(submit).click()



GoogleLogin("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin","/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]", Email, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input", "/html/body/div[1]/div[2]/div/div[2]/form/span/div/div[2]/input", Password, "/html/body/div[1]/div[2]/div/div[2]/form/span/div/input[2]")
GmailNav("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[2]/div[2]/form/div/table/tbody/tr/td/table/tbody/tr/td/div/input[1]", "//html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr[1]", "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[3]/table/tbody/tr/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/a")
RuvnaForm("/html/body/div[2]/div/div/div/div[1]/div[3]/a/div","/html/body/div[2]/div/div/div/div[2]/div[3]/div[3]/div[2]/div/div[2]","/html/body/div[2]/div/div/div/div[2]/div[3]/div[3]/div[3]/div/div[2]","/html/body/div[2]/div/div/div/div[2]/div[3]/div[3]/div[4]/div/div[2]","/html/body/div[2]/div/div/div/div[2]/div[3]/div[3]/div[5]/button")