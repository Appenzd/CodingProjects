from __future__ import print_function
from selenium import webdriver
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import time
import boto3
import keyboard
import unidecode




#login
Email = "***"
Password = "***"
#incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("/Users/danielappenzeller/dev/coding/webtest/chromedriver", options=chrome_options)

#sheets setup
scopes = ['https://www.googleapis.com/auth/drive']
spreadsheetID = '1UFOrkXczroTLwPExiHejsXmbJ25gJF7QhCHZ3SGCRNI'
rangeID = 'A1:E1'
values = [
	["Name", ],
	["Email",],
	["Parent1",],
	["Parent2",],
	["Address",],
]

#aws setup
# bucket='crystal-springs-photos'
# collection_id='crystalimages'
# image=""
# client=boto3.client('rekognition')

# client.delete_collection(CollectionId=collection_id)
# response=client.create_collection(CollectionId=collection_id)

#misc
classnum = 2
delay = 0


#Login to Crystal Springs website
def CrystalLogin(url,usernameID, username, loginbutton1,loginbutton2,passwordId, password, loginbutton3):
	driver.get(url)
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_id(usernameID):
			driver.find_element_by_id(usernameID).send_keys(username)
			break
		if delay <= time.time():
			break
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_id(loginbutton1):
			driver.find_element_by_id(loginbutton1).click()
			break
		if delay <= time.time():
			break		
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_id(loginbutton2):
			driver.find_element_by_id(loginbutton2).click()
			break
		if delay <= time.time():
			break	
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_name(passwordId):
			time.sleep(.5)
			driver.find_element_by_name(passwordId).send_keys(password)
			break
		if delay <= time.time():
			break				
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_id(loginbutton3):
			driver.find_element_by_id(loginbutton3).click()
			time.sleep(10)
			break
		if delay <= time.time():
			break

#main Loop for Web Scraping
def ScrapeLoop():
	#setup
	global rangeID
	global client
	driver.execute_script("window.scrollTo(0, 0)") 
	while not driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[1]/a"):
		time.sleep(.01)
		driver.execute_script("window.scrollTo(0, 0)")
	driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[1]/a").click()
	driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[" + str(classnum) + "]/a").click()
	time.sleep(1)
	nameNum = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[1]/div").text
	nameInt = str(nameNum[0]) + str(nameNum[1])
	rangeID = "A1:E" + str(int(nameInt) + 100)
	nameCount = 1
	
	#Load Entire webpage
	x = 0
	while x != 5:
		time.sleep(.5)
		driver.execute_script("window.scrollTo(0, 100000)") 
		x = x + 1
	driver.execute_script("window.scrollTo(0, 0)") 
	for i in range(int(nameInt)):
		#Additional Informaition
		while not driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[1]"):
				time.sleep(.001)
		driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[1]").click()
		#Name
		while not driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/h3"):
				time.sleep(.01)
		value = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/h3").text
		value = value.replace(" '" + str(-classnum + 30), "")
		values[0].append(value)

		# #Photo
		# while not driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[1]/div/img"):
		# 		time.sleep(.01)
		# image = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[1]/div/img").screenshot("crystalimage.png")
		# client = boto3.client('s3', region_name='us-west-1')
		# client.upload_file('/Users/danielappenzeller/dev/coding/aws/crystalimage.png', bucket, "crystalimage.png")

		# client=boto3.client('rekognition')
		# client.index_faces(CollectionId=collection_id,Image={'S3Object':{'Bucket':bucket,'Name':"crystalimage.png"}},ExternalImageId=unidecode.unidecode(value.replace(" ","").replace("'","")))

		#Email
		delay = time.time() + 5
		while True: 
			if driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/p[1]/a"):
				value = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/p[1]/a").text
				values[1].append(value)
				break
			if delay <= time.time():
				values[1].append("None")
				break	

		#Parent1
		delay = time.time() + 5
		while True:
			if driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td/div[1]/div[2]/h4"):
				value = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td/div[1]/div[2]/h4").text
				value = value.replace(" (Parent)", "")
				values[2].append(value)
				break
			if delay <= time.time():
				values[2].append("None")
				break	
		#Parent2
		delay = time.time() + 5
		while True:
			if driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td/div[1]/div[2]/h4"):
				value = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td/div[1]/div[2]/h4").text
				value = value.replace(" (Parent)", "")
				values[3].append(value)
				break
			if delay <= time.time():
				values[3].append("None")
				break
		#Address
		if driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/p"):
			value = driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(nameCount) + "]/td[2]/div[2]/div/div[3]/div/p").text
			if "H:" in value:
				value = value.split("H:")[0]
				value = value[:-1]
			if "C:" in value:
				value = value.split("C:")[0]
				value = value[:-1]
			if value == "" or value == " ":
				values[4].append("None")
			else:
				values[4].append(value)
		else:
			values[4].append("None")
		nameCount = nameCount + 1 
def Sheets():
	global rangeID
	creds = Credentials.from_authorized_user_file('token.json', scopes)
	service = build('sheets', 'v4', credentials=creds)
	sheet = service.spreadsheets()
	body = {
		'majorDimension': 'COLUMNS',
		'values': values
	}
	if classnum != 9:
		request_body = {
	            'requests': [{
	                'addSheet': {
	                    'properties': {
	                        'title': str(classnum + 4) + "thGrade",
	                    }
	                }
	            }]
	    }
	rangeID = str(classnum + 4) + "thGrade!" + rangeID
	response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetID, body=request_body).execute()
	result = service.spreadsheets().values().update(spreadsheetId=spreadsheetID, valueInputOption='USER_ENTERED', range=rangeID, body=body).execute()

# while True:
# 	CrystalLogin("https://csus.myschoolapp.com/app#login", "Username", Email, "nextBtn", "identifierNext", "password", Password, "passwordNext")
# 	if driver.current_url == "https://csus.myschoolapp.com/app/student#studentmyday/assignment-center":
# 		break
# driver.get('https://csus.myschoolapp.com/app/student#directory/465')
# while not driver.find_elements_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[2]/a"):
# 	time.sleep(.01)
# driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[2]/a").click()
# driver.find_element_by_xpath("/html/body/div[3]/div/div[13]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/section/div[2]/ul/li[9]/a/div").click()
# while classnum != 9:
# 	ScrapeLoop()
# 	Sheets()
# 	values = [
# 		["Name", ],
# 		["Email",],
# 		["Parent1",],
# 		["Parent2",],
# 		["Address",],
# 	]
# 	classnum = classnum + 1


def GoogleLogin():
	driver.get("https://www.google.com/maps/d/u/1/?hl=en")
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"):
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("daniel@appenzeller.net")
			break
		if delay <= time.time():
			break
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"):
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
			break
		if delay <= time.time():
			break		
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div"):
			time.sleep(1)
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[1]/div").click()
			break
		if delay <= time.time():
			break	
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"):
			time.sleep(.5)
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("*Gh9tP-hET")
			break
		if delay <= time.time():
			break				
	delay = time.time() + 10
	while True: 
		if driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"):
			driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
			time.sleep(3)
			break
		if delay <= time.time():
			break

def MapInput():
	driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/span/span").click()

	creds = Credentials.from_authorized_user_file('token.json', scopes)
	service = build('sheets', 'v4', credentials=creds)
	sheet = service.spreadsheets()

	classnum = 6

	while classnum != 13:
		result = sheet.values().get(spreadsheetId="1UFOrkXczroTLwPExiHejsXmbJ25gJF7QhCHZ3SGCRNI",range=str(classnum) + "thGrade!E2:E100").execute()
		addresslist = result.get("values", []) 
		driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[9]/div/div[2]/div[1]/div/ul/li[1]").click()
		for address in addresslist:
			while True: 
				time.sleep(1)
				if driver.find_elements_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[4]/div[1]/div/div/form/input"):
					if "None" in address:
						break
					driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[4]/div[1]/div/div/form/input").send_keys(address)
					driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[4]/div[1]/div/div/form/div/div/img").click()
					delay = time.time() + 10
					while True: 
						time.sleep(1)
						if driver.find_elements_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[2]/div[3]/div/div[4]/div[2]/div/div/div/div/div/div[3]"):
							
							driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div[1]/div/div[2]/div[3]/div/div[4]/div[2]/div/div/div/div/div/div[3]").click()
							break
						if delay <= time.time():
							break
					break
		classnum = classnum + 1

GoogleLogin()
MapInput()

