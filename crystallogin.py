from selenium import webdriver
import time


Email = "***"
Password = "***"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("***", options=chrome_options)

def login(url,usernameID, username, loginbutton):
   driver.get(url)
   time.sleep(2) 
   driver.find_element_by_id(usernameID).send_keys(username)
   time.sleep(.1) 
   driver.find_element_by_id(loginbutton).click()
   time.sleep(3) 
def GoogleEmaillogin(loginbutton):
   driver.find_element_by_id(loginbutton).click()
   time.sleep(2) 
def GooglePasslogin(passwordId, password, loginbutton):
   driver.find_element_by_name(passwordId).send_keys(password)
   time.sleep(.1) 
   driver.find_element_by_id(loginbutton).click()
   time.sleep(.1) 


login("https://csus.myschoolapp.com/app#login", "Username", Email, "nextBtn")
GoogleEmaillogin("identifierNext")
GooglePasslogin("password", Password, "passwordNext") 


		
