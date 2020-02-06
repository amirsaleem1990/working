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
###########################################
import signal
def print_linenum(signum, frame):
    print ("Currently at line", frame.f_lineno)
signal.signal(signal.SIGINT, print_linenum)
###########################################
with open("/home/amir/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
    usrname, pas = file.read().splitlines()

try_for_success_fully_logedin = True

while try_for_success_fully_logedin:
	try:
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

		try_for_success_fully_logedin = False
	except:
		pass

errors = []
succussfully_extracted = 0

os.system("ipython3 /home/amir/github/working/Facebook_posts_links/links-pickle-to-df.py")
df = pd.read_csv("/home/amir/github/working/Facebook_posts_links/All_FB_links_names_corrected.csv")

os.chdir("/home/amir/github/working/Facebook_posts_links/")
a = ''.join(list(os.popen("cat *.txt")))
indexes = [e for e,i in enumerate(df.Link) if not i in a]
to_scrap = df.iloc[indexes]
print(f"\nThere is {len(to_scrap)} to scrap\n")
ids_removed_from_facebook = ["abumaryam82", "hammad.sarwar.9400"]
for name in to_scrap.Name.unique():
	if not name in ids_removed_from_facebook:
		print("\n", "*"*30, name, "*"*30)
		name_df = to_scrap[to_scrap.Name == name]
		file_name = f"{name}.txt"
		file_exist =  file_name in os.listdir()
		if file_exist:
			with open(file_name, "r") as file:
				exist = file.read()
			file.close()
		for e, link in enumerate(name_df.Link):
			print(e, end="|")
			if file_exist:
				if link in exist:
					continue
			try:
				browser.get(link)
			except:
				errors.append([name, link])
				continue
			soup = BeautifulSoup(browser.page_source, "lxml")
			try:
				a = soup.find("div", {"class" : "_5wj-"}).text
				if len(a) > 0:
					file = open(file_name, "a+")
					file.write("\n" + "#"*30 + "\n")
					file.write(link + "\n")
					file.write(a + "\n")
					succussfully_extracted += 1
					file.close()
				else:
					errors.append([name, link])
			except:
				errors.append([name, link])
				pass
print("\n\nsuccussfully extracted: ", succussfully_extracted)
if errors:
	with open("errors.pkl", "wb") as file:
		pickle.dump(errors, file)
	print(f"\n\nThere is {len(errors)} errors, saved in <errors.pkl>\n\n")