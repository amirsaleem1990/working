import os
import pandas as pd
import time
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import itertools
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# need to open links or not?
read_or_not = input("Are you need to open new links? [y/n]\n")	

options = Options()
options.add_argument("--headless")
    
with open("/home/amir/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
    usrname, pas = file.read().splitlines()
    
# browser = webdriver.Firefox(executable_path="/home/amir/github/working/Facebook_posts_links/geckodriver")
browser = webdriver.Firefox(executable_path="/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)
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

link_dict = {}
fb_base_url = "https://web.facebook.com/"
# pages i nedd in list: "idreesazad2"
counter = 0
names = ["Mushtaq", "Asif mehmood", "Zahid mughal", "Mohammad Fahad Haris", "Abdullah Adam", "Hm Zubair", "Muhammad Imran", "Munib Hussain", "Jameel Baloch",
	 "Rizwan Asad Khan", "Abubakr Quddusi", "Mohammad Din Jauhar", "Riayatullah Farooqui", "Asim AllahBakhsh", "Sohaib naseem", "Idrees Aazad", 
	 "Abu muhammad musab", "Mahtab khan", "mohammad.saleem"]
urls = ["MMushtaqYusufzai", "asif.mahmood.1671", "zahid.mughal.5895", 
     "mohammad.f.haris", "abdullah.adam49", "hm.zubair.52", 
      "abumaryam82", "munib.hussain86", "jameelbaloch1924", 
      "theguided1", "abubakr.quddusi.3",
     "mohammaddin.jauhar.7", "Riayat.Farooqui", "asim.allahbakhsh",
     "sohaib.naseem.3", "idreesazaad", "Abu.Musab.98622733", 
     "profile.php?id=100026041448813", "mohammad.saleem.568847"]
for name, url in zip(names, urls):
	counter += 1
	print("Done: ", round(counter / len(names), 2), "% || ", counter, "out of ", len(names))
    complted_url = fb_base_url + url
    if not name in link_dict:
        link_dict[name] = []
    browser.get(complted_url)
    s = BeautifulSoup(browser.page_source, "lxml")
    a = s.find("div", {"id" : "timeline_story_column"})
    for i in a.find_all('a'):
        try:
            if (i['href'].startswith(complted_url + "/post")) and (not "comment_id" in i['href']):
                if not i['href'] in all_links[name]:
                    link_dict[name].append(i['href'])
        except:
            pass

if not list(itertools.chain(*link_dict.values())):
    print("\n\n\nNOTE: there is no new link\n\n")

else:
    with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "wb") as file:
        pickle.dump(link_dict, file)


browser.close()
os.remove("geckodriver.log")

if read_or_not.lower() == "y":
	import Open_FB_links
	Open_FB_links.open_links()
elif read_or_not.lower() == "n":
	pass