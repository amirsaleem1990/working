import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import time
import pandas as pd
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")

os.system("clear")

with open("/home/amir/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
    usrname, pas = file.read().splitlines()

# browser = webdriver.Firefox(executable_path=home + "/github/working/Facebook_posts_links/geckodriver")
browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options= options)
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

os.system("ipython3 links-pickle-to-df.py")
df = pd.read_csv("All_FB_links_names_corrected.csv")
for e, name in enumerate(df.Name.unique()):
	name_df = df[df.Name == name]
	os.mkdir(name)
	os.chdir(name)
	for link in name_df.Link:
		browser.get(link)
		soup = BeautifulSoup(browser.page_source, "lxml")
		a = soup.find("div", {"class" : "_5wj-"}).text
		if not a:
			print("Fail: ", name, link)
			continue
		with open(f"{e}.txt", "w") as file:
			file.write(a)
		time.sleep(2)
	os.chdir("../")