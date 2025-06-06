#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()

def current_time():
	import datetime
	return ''.join(str(datetime.datetime.now()).split()[1].split(".")[:-1])

def LOGIN(visual=False):
	import numpy as np
	import time
	print("Attempting to Login   ", current_time())
	Successfully_logedin = True
	Successfully_logedin_num = 0
	# if input("Are u need visual tracking? [y\\n]:\t").lower() == "y":
		# visual = True
	# else:
	from selenium.webdriver.firefox.options import Options
	options = Options()
	options.add_argument("--headless")
		
	while Successfully_logedin:
		Successfully_logedin_num += 1
		if Successfully_logedin_num > 1:
			print(f"Attempt no. {Successfully_logedin_num} to Login")
		try:
			if visual:
				browser = webdriver.Firefox(executable_path = "/home/amir/github/Linux/bin/functional/geckodriver")
			else:
				browser = webdriver.Firefox(executable_path = "/home/amir/github/Linux/bin/functional/geckodriver", options=options)	

			#navigates you to the facebook page.
			browser.get('https://www.facebook.com/')

			#find the username field and enter the email example@yahoo.com.
			time.sleep(np.random.randint(3, 6))
			username = browser.find_elements_by_css_selector("input[name=email]")
			username[0].send_keys(usrname)


			#find the password field and enter the password password.
			time.sleep(np.random.randint(3, 6))
			password = browser.find_elements_by_css_selector("input[name=pass]")
			password[0].send_keys(pas)


			#find the login button and click it.
			time.sleep(np.random.randint(3, 6))
			loginButton = browser.find_elements_by_css_selector("button[ type=submit]")
			loginButton[0].click()
			print("Successfully Logged in", current_time())
			Successfully_logedin = False
		except:
			print(traceback.format_exc())
			pass

	return browser