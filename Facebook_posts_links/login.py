#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()
def current_time():
	import datetime
	n = datetime.datetime.now()
	t = ':'.join([str(i) for i in [n.hour % 12, n.minute, n.second]])
	tt = ""
	for i in t.split(":"):
		if len(i) == 1:
			tt += "0" + i
		else:
			tt += i
		tt += ":"
	tt = tt.strip(":")
	return tt
def LOGIN():
	print("Attempting to Login   ", current_time())
	Successfully_logedin = True
	Successfully_logedin_num = 0
	# if input("Are u need visual tracking? [y\\n]:\t").lower() == "y":
		# visual = True
	# else:
	from selenium.webdriver.firefox.options import Options
	options = Options()
	options.add_argument("--headless")
	visual = True
		
	while Successfully_logedin:
		Successfully_logedin_num += 1
		if Successfully_logedin_num > 1:
			print(f"Attempt no. {Successfully_logedin_num} to Login")
		try:
			if visual:
				browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver")
			else:
				browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)	

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
			loginButton = browser.find_elements_by_css_selector("input[type=submit]")
			loginButton[0].click()
			print("Successfully Logged in", current_time())
			Successfully_logedin = False
		except:
			pass

return browser