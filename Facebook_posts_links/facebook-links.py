import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")

with open("/home/amir/github/working/Facebook_posts_links/All_FB_links.pkl", "rb") as file:
    all_links = pickle.load(file)
    
all_links_list = []
for i in all_links:
    all_links_list += all_links[i]


with open("/home/amir/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
    usrname, pas = file.read().splitlines()
print("Attempting to Login")
print(str(datetime.datetime.now()))
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
print("Successfully Logged in")
print(str(datetime.datetime.now()))
# pages i nedd in list: "idreesazad2"
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

fb_base_url = "https://web.facebook.com/"
extrected_links = []
new_links = []
counter = 0
for name, url in zip(names, urls):
	counter += 1
	print((counter / len(names))*100, "%", print(str(datetime.datetime.now())))
	complted_url = fb_base_url + url
	if not name in all_links:
		all_links[name] = []
	browser.get(complted_url)
	s = BeautifulSoup(browser.page_source, "lxml")
	a = s.find("div", {"id" : "timeline_story_column"})
	try:
		print(a.find_all('a').get('href') )
	except:
		pass
	# for i in a.select('a'):
	# 	for z in i:
	# 		try:
	# 			# extrected_links.append(z['href'])
	# 			# print(z.get("href"))
	# 			# if not "https://web.facebook.com" + link in all_links_list:
	# 			# 	if link != "#":
	# 			# 		if not link.startswith("/ufi"):
	# 			# 			if not link.startswith("http"):
	# 			# 				if not link.startswith("/profile"):
	# 			# 					if "/posts/" in link:
	# 			# 						new_links.append(link)
	# 			# 						all_links[name].append("https://web.facebook.com" + link)
	# 		except:
	# 			pass

# with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "wb") as file:
#     pickle.dump(new_links, file)
# with open("/home/amir/github/working/Facebook_posts_links/All_FB_links.pkl", "wb") as file:
# 	pickle.dump(all_links, file)
# browser.close()
# os.remove("geckodriver.log")