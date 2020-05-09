import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import sys
import datetime
from selenium.webdriver.common.keys import Keys

import sys
sys.path.insert(0,'/home/amir/github/working/Facebook_posts_links/')
from functions import *

# os.chdir("/home/amir/github/working/Facebook_posts_links/get_all_links_for_user/0-get-timeline-and-further-links")

qty_of_pages = int(input("Enter pages Qty for each profile: "))

os.system("clear")

FB = [i.split("\t")[0].strip() for i in open("/home/amir/github/working/Facebook_posts_links/FB.txt", "r").read().splitlines()]

all_links = pickle.load(open("/home/amir/github/working/Facebook_posts_links/All_FB_links_names_corrected.pkl", "rb"))
ids_removed_from_facebook = pickle.load(
	open("/home/amir/github/working/Facebook_posts_links/ids_removed_from_facebook.pkl", "rb"))

usrname, pas = open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r").read().splitlines()

stored_links_qty = sum([len(all_links[i]) for i in all_links])	

fb_base_url = "https://m.facebook.com/"

browser = LOGIN(usrname, pas, fb_base_url)

ids_removed_from_facebook = list(ids_removed_from_facebook.keys())

extrected_links = []
new_links = []
mmz = []
errors = []
links_to_open = []



counter = 0
succussfully_extracted = 0

def get_next_page_link(LINK):
	global c
	global next_page_error
	global Errors_dict
	c += 1
	try:
		browser.get(LINK)
		s = BeautifulSoup(browser.page_source, "lxml")
		try:
			next_page_link = fb_base_url.strip("/")  + s.find("div", {"id" : "u_0_3"}).find("a")['href']
		except:
			try:
				next_page_link = fb_base_url.strip("/")  + s.find("div", {"id" : "u_0_0"}).find("a")['href']
			except:
				try:
					next_page_link = fb_base_url.strip("/")  + s.find("div", {"id" : "u_0_2"}).find("a")['href']
				except:
					next_page_link = fb_base_url.strip("/")  + s.find("div", {"id" : "u_0_1"}).find("a")['href']
		pages_links.append(next_page_link)

		to_save = str(s)
		pickle.dump(to_save, open(f"{folder_name}/{len(pages_links)}_{fb}.pkl", "wb"))
		next_page_error = 0
	except:
		next_page_error += 1
		Errors_dict["next page Error"].append(LINK)

Errors_dict = {"another Error" : [], 
				"next page Error" : [], 
				"ID not found" : []}


FB = [i for i in FB if i in ["MMushtaqYusufzai", "profile.php?id=100026041448813", "profile.php?id=100032249983289", "anas.islam.3551", "tariq.habib.969952", "groups/pakdotai/", "profile.php?id=100010345081577", "athar.w.azeem", "Nassim.Haramein.official", "rehan.umar.165", "groups/2963990780318681/"]]
for fb in FB:
	next_page_error = 0
	try:
		print(fb)
		folder_name = "/home/amir/github/working/Facebook_posts_links/get_all_links_for_user/Extracted/" + fb
		try:
			os.mkdir(folder_name)
		except:
			pass

		complted_url = fb_base_url + fb

		try:
			browser.get(complted_url)
		except:
			Errors_dict["ID not found"].append(fb)
			continue # sys.exit()
		s = BeautifulSoup(browser.page_source, "lxml")

		for i in s.find("div", {"class" : "bl"}).select("div", {"class" : "cv"}):
			try: 
				link_ = i.find("a")['href']
				if "timeline&lst" in link_:
					time_line_link = fb_base_url.strip("/") + link_
					break
			except: 
				pass

		pages_links = []
		pages_links.append(time_line_link)

		c = 0
		while c < qty_of_pages: # only first few pages
			c += 1 
			get_next_page_link(pages_links[-1])
			time.sleep(2)
			if next_page_error > 2:
				break
		pickle.dump(pages_links,  open(f"{folder_name}/LINKS.pkl", "wb"))
		print(f"succussfully COMPLETED {fb}")
	except:
		Errors_dict["another Error"].append(fb)
		pass

print("\n\n\n")
for i in Errors_dict:
	if Errors_dict[i]:
		print(i)
		print(Errors_dict[i])
		print("******************************")