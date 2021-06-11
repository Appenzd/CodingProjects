from selenium import webdriver
import time
import keyboard


#incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("/Users/danielappenzeller/dev/coding/webtest/chromedriver")

x = 0

def start(url, startbutton):
   driver.get(url)
   driver.find_element_by_xpath(startbutton).click()
   time.sleep(3) 
def equationFunc(equationID, enterbutton):
    equation = driver.find_element_by_id(equationID).text
    equation = equation[:-1]
    equation = equation.replace("x","*")
    answer = eval(equation)
    for char in str(answer):
   		keyboard.press_and_release(char) 
    driver.find_element_by_xpath(enterbutton).click()

start("https://www.timestables.com/100-seconds/", "/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/a")

while x != 1000000000000000:
	equationFunc("somVakHonderd", "/html/body/div[3]/div/div/div[2]/div/div[3]/div[7]/a")
	x = x+1




		
