from selenium import webdriver
import boto3
import time
import keyboard

x = 0

Username = "***"
Password = "***"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("/Users/danielappenzeller/dev/coding/webtest/chromedriver", options=chrome_options)


def login(usernameID, username, passwordID, password, loginbutton):
   driver.get("https://www.nitrotype.com/login")
   driver.find_element_by_xpath(usernameID).send_keys(username)
   driver.find_element_by_xpath(passwordID).send_keys(password)
   driver.find_element_by_xpath(loginbutton).click()
def start(startrace):
   time.sleep(1)
   driver.find_element_by_xpath(startrace).click()
   time.sleep(2)






login("/html/body/div[1]/div/div/main/div/section/div[2]/div/div[3]/form/div[1]/div[1]/div[2]/input", Username, "/html/body/div[1]/div/div/main/div/section/div[2]/div/div[3]/form/div[1]/div[2]/div[2]/input", Password, "/html/body/div[1]/div/div/main/div/section/div[2]/div/div[3]/form/button")
start("/html/body/div/div/header/div/div[3]/div[1]/a")
while x != 1000:
	while not driver.find_elements_by_xpath("/html/body/div[1]/div/main/div/section/div[1]/div[2]/div[3]/div/div[2]/button"):
		
		if driver.find_elements_by_xpath("/html/body/div/div/main/div/section/div[3]/div[1]/div[1]/div[2]/div[1]"):

			driver.find_element_by_xpath("/html/body/div/div/main/div/section/div[3]/div[1]/div[1]/div[2]/div[1]").screenshot("nitrotype.png")
			documentName = "nitrotype.png"

			with open(documentName, 'rb') as document:
			    imageBytes = bytearray(document.read())
			textract = boto3.client('textract')
			response = textract.detect_document_text(Document={'Bytes': imageBytes})

			for item in response["Blocks"]:
				if item["BlockType"] == "LINE":
					time.sleep(1)
					keyboard.write(item["Text"])
					keyboard.press_and_release('space')
	driver.find_element_by_xpath("/html/body/div[1]/div/main/div/section/div[1]/div[2]/div[3]/div/div[2]/button").click()
	x = x + 1


		




