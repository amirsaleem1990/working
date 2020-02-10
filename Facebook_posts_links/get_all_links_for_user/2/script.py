import pandas as pd
import requests
from bs4 import BeautifulSoup
import pickle
import os
import time
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")


os.system("clear")
with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()
Successfully_logedin = True
Successfully_logedin_num = 0
while Successfully_logedin:
	Successfully_logedin_num += 1
	if Successfully_logedin_num > 1:
		print(f"Attempt no. {Successfully_logedin_num} to Login")
	try:
		browser = webdriver.Firefox(executable_path="../geckodriver")
		# browser = webdriver.Firefox(executable_path = "../geckodriver", options=options)
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
		print("Successfully Logged in")
		Successfully_logedin = False
	except:
		pass

errors = []
df = pd.read_csv("../Links.csv")
for unique_name in df.Name.unique():
	if not unique_name in ["mohammad.f.haris", "Riayat.Farooqui", "theguided1", "hm.zubair.52", "munib.hussain86"]:
		print("************************************************************************")
		print(unique_name)
		try:
			local_df = df[df.Name == unique_name]
			for i in local_df.iterrows():
				name = i[1][0]
				link = i[1][1]
				file_name = f"{name}.txt"
				try:
					existing = open(file_name).read()
				except:
					existing = ""
				if not link in existing:
					try:
						time.sleep(1)
						browser.get(link)
					except:
						errors.append([name, link])
						continue
					try:
						soup = BeautifulSoup(browser.page_source, "lxml")
						aa = soup.find("div", {"class" : "_5wj-"}).text
						if len(aa) > 0:
							file = open(file_name, "a+")
							file.write("\n" + "#"*30 + "\n")
							file.write(link + "\n")
							file.write(aa + "\n")
							file.close()
						else:
							errors.append([name, link])
					except:
						errors.append([name, link])
						pass
		except:
			print(f"Error: {name}")

