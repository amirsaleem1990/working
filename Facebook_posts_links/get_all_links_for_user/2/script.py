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


import sys
sys.path.insert(0,'/home/amir/github/working/Facebook_posts_links/')
from functions import *

os.system("clear")
with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()

fb_base_url = "https://www.facebook.com/"
browser = LOGIN(usrname, pas, fb_base_url)

errors = []
df = pd.read_csv("/home/amir/github/working/Facebook_posts_links/get_all_links_for_user/1-facebook-users-all-posts-links/Links.csv")
for unique_name in df.Name.unique():
	print("************************************************************************")
	print(unique_name)
	try:
		local_df = df[df.Name == unique_name]
		for i in local_df.iterrows():
			name = i[1][0]
			link = i[1][1]
			file_name = f"/home/amir/github/working/Facebook_posts_links/{name}.txt"
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