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

os.system("clear")

FB = [i.split("\t")[0].strip() for i in open("/home/amir/github/working/Facebook_posts_links/FB.txt", "r").read().splitlines()]

all_links = pickle.load(open("/home/amir/github/working/Facebook_posts_links/All_FB_links_names_corrected.pkl", "rb"))
ids_removed_from_facebook = pickle.load(
	open("/home/amir/github/working/Facebook_posts_links/ids_removed_from_facebook.pkl", "rb"))

usrname, pas = open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r").read().splitlines()

stored_links_qty = sum([len(all_links[i]) for i in all_links])	

browser = LOGIN(usrname, pas)

ids_removed_from_facebook = list(ids_removed_from_facebook.keys())

extrected_links = []
new_links = []
counter = 0
links_to_open = []


mmz = []
errors = []

succussfully_extracted = 0

def get_next_page_link(LINK):
    global c
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

    except:
        print("ERROR: ",fb, LINK)
        import sys
        sys.exit()


for fb in FB:
    try:
        print(fb)
        folder_name = "/home/amir/github/working/Facebook_posts_links/get_all_links_for_user/Extracted/" + fb
        os.mkdir(folder_name)
        complted_url = fb_base_url + fb

        try:
            browser.get(complted_url)
        except:
            print("ID not found", fb)
            sys.exit()
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

        while c < 20:
            get_next_page_link(pages_links[-1])
            time.sleep(2)
            c += 1 # only first few pages
        pickle.dump(pages_links,  open(f"{folder_name}/LINKS.pkl", "wb"))

    except:
        print("Error in: ", fb)
        pass