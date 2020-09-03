#!/usr/bin/python3
import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import datetime
from login import LOGIN

try:
	import sys
	argument=bool(sys.argv[1])
except:
	# default is False
	argument = False
def write_to_file(file_name, link, post):
	file = open(file_name, "a+")
	file.write("\n" + "#"*30 + "\n")
	file.write(link + "\n")
	file.write(post + "\n")
	file.close()

# os.chdir("/home/amir/github/Daily_facebook/")
os.system("clear")
browser = LOGIN(argument)
fb_base_url = "https://web.facebook.com/"
now = datetime.datetime.now()
# linkS = open("ay_links_to_copy.txt", "r").read().splitlines()
file_ = input("Enter .txt file name which is contains facebook links")
linkS = open(file_, "r").read().splitlines()


file_name = input("Enter output file name: ")
while os.path.exists(file_name):
	file_name = input("This file is Already exist, please new name: ")

for e, link in enumerate(linkS):
	print(f"Completed {e},   {round(e/len(linkS)*100)}")
	browser.get(link)
	soup = BeautifulSoup(browser.page_source, "lxml")
	try:
		try:
			aa = soup.find("div", {"data-testid" : "post_message"}).text
		except:
			aa = soup.find("div", {"class" : "_5wj-"}).text
		try:		
			if len(aa) > 0:
				write_to_file(file_name, link, aa)
		except:
			import traceback
			print(traceback.format_exc())
			print('---------------')
	except:
		pass

browser.close()

try:
	os.remove("geckodriver.log")
except:
	pass