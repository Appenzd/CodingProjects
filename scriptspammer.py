import time
import keyboard


Script = open("Script.txt")

time.sleep(5)

for line in Script:
	for char in line:
		if char == " ":
			keyboard.press_and_release("enter")
			# time.sleep(1)
		keyboard.press_and_release(char)


	  
