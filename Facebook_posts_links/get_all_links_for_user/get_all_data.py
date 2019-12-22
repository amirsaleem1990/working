import pandas as pd
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


def posts(soup, fb):
	try:
		a = soup.find("div", {"id" : "structured_composer_async_container"}).find("div", {"class" : "bm bn bo"})
		posts = a.findAll("div", {"class" : "bp bq br"})
	except:
		print(f"{fb}: Main page Error")
		return None
	for post in posts:
		try:
			date = post.find("div", {"class" : "cg ch"}).find("abbr").text
			post_contant = post.find("div", {"class" : "ca"}).text
			ab2 = post.find("a")['href'].split("story_key.")[1]
			post_link = f"https://web.facebook.com/{fb}/posts/" + ab2[:ab2.find("%")]
			Data = {"Date" : date,
					"Post" : post_contant,
					"Link" : post_link,
					"Name" : fb}
		except:
			return None
	all_data.append(Data)



os.chdir("/home/amir/github/working/Facebook_posts_links/")

os.system("clear")

def current_time():
	n = datetime.datetime.now()
	t = ':'.join([str(i) for i in [n.hour, n.minute, n.second]])
	tt = ""
	for i in t.split(":"):
		if len(i) == 1:
			tt += "0" + i
		else:
			tt += i
		tt += ":"
	tt = tt.strip(":")
	return tt

with open("All_FB_links_names_corrected.pkl", "rb") as file:
	all_links = pickle.load(file)

stored_links_qty = sum([len(all_links[i]) for i in all_links])	

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()

print("Attempting to Login", current_time())
# browser = webdriver.Firefox(executable_path="/home/amir/github/working/Facebook_posts_links/geckodriver")
browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)
#navigates you to the facebook page.
browser.get('https://m.facebook.com/')

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

#find the OK button and click it.
time.sleep(np.random.randint(3, 6))
loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()


print("Successfully Logged in", current_time())
FB = ["MMushtaqYusufzai", 					# Muhammad Mushtaq
		"asif.mahmood.1671", 				# asif mahmood
		"zahid.mughal.5895", 				# zahid mughal
		"mohammad.f.haris", 				# mohammad fahad haris
		"abdullah.adam49", 					# abdullah adam 
		"hm.zubair.52", 					# Hm Zubair 
		"abumaryam82",  					# Muhammad Imran (Blocked)
		"yaldrim.khalid.9", 				# Muhammad Imran
		"munib.hussain86", 					# munib hussain 
		"jameelbaloch1924", 				# jameel baloch 
		"theguided1",  						# Rizwan Asad Khan
		"abubakr.quddusi.3", 				# abubakr quddusi 
		"mohammaddin.jauhar.7", 			# mohammad din jauhar 
		"Riayat.Farooqui",  				# riayatullah farooqui 
		"asim.allahbakhsh", 				# asim allahbakhsh 
		"sohaib.naseem.3", 					# صہیب نسیم‎  
		"idreesazaad", 						# Idrees Azad ‎
		"Abu.Musab.98622733", 				# ابو محمد مصعب 
		"profile.php?id=100026041448813", 
		"mohammad.saleem.568847", 			# mohammad saleem 
		"hammad.sarwar.9400",
		"ajeebscenehaibhai", 
		"nouman.atd.3", 					# Nouman Ihsan
		"profile.php?id=100032249983289", 	# انس اسلام
		"HamidKamaluddin.personal", 		# Hamid kamaluddin
		"faisal.shahzad.1253236", 			# محمد فیصل شہزاد
		"tariq.habib.969952", 				# tariq habib
		"mahtabaziz", 						# mahtab khan
		"suhaib.jamal.1" 					# Suhaib Jamal
	  ]
fb_base_url = 'https://m.facebook.com/'
all_data = []
errors_first_page = []
for e, fb in enumerate(FB):
	time.sleep(np.random.randint(3, 6))
	complted_url = fb_base_url + fb
	print(e, len(all_data))
	try:
		browser.get(complted_url)
		s_Main_page = BeautifulSoup(browser.page_source, "lxml")

		for i in s_Main_page.select("div", {"class" : "cs g ch"}):
			try:
				link = i.find("a")['href']
				if link.startswith(f"/{fb}?v=timeline&lst="):
					timeline_LINK = "https://mobile.facebook.com" + link
			except:
				continue
		try:
			timeline_LINK
		except:
			print(f"{fb}: No timeline Link")
			continue
			
		browser.get(timeline_LINK)
		del timeline_LINK
		
		s_first_page = BeautifulSoup(browser.page_source, "lxml")
		posts(s_first_page, fb)
	except:
		continue
		
	next_page_link = "https://mobile.facebook.com" + s_first_page.find("div", {"id" : "u_0_3"}).find("a")['href']
	while True:
		try:
			time.sleep(np.random.randint(2, 4))
			browser.get(next_page_link)
			s_next_page = BeautifulSoup(browser.page_source, "lxml")
			posts(s_next_page, fb)
			next_page_link = "https://mobile.facebook.com" + s_next_page.find("div", {"id" : "u_0_3"}).find("a")['href']
		except:
			break