def next_page(link, c, fb):
    browser.get(link)
    page = BeautifulSoup(browser.page_source, "lxml")

    file_name = f"{folder}/{c}_{fb}.pkl"
    with open(file_name, "wb") as file:
        pickle.dump(str(page), file)
    next_page_link = "https://mobile.facebook.com" + page.find("div", {"id" : "u_0_0"}).find("a")['href']
    links.append(next_page_link)
    print(len(set(links)), end=" | ")
    return next_page_link

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

os.chdir("/home/amir/github/working/Facebook_posts_links/")

os.system("clear")

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
    usrname, pas = file.read().splitlines()

print("Attempting to Login")
browser = webdriver.Firefox(executable_path="/home/amir/github/working/Facebook_posts_links/geckodriver")
# browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)
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


print("Successfully Logged in")

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
		"mohammad.saleem.568847", 			# mohammad saleem (Blocked) 
	    "profile.php?id=100010667655748", 	# mohammad saleem
		"hammad.sarwar.9400",
		"ajeebscenehaibhai", 
		"nouman.atd.3", 					# Nouman Ihsan
		"profile.php?id=100032249983289", 	# انس اسلام
		"HamidKamaluddin.personal", 		# Hamid kamaluddin
		"faisal.shahzad.1253236", 			# محمد فیصل شہزاد
		"tariq.habib.969952", 				# tariq habib
		"mahtabaziz", 						# mahtab khan
		"suhaib.jamal.1", 					# Suhaib Jamal
	    "hanifsamanaa"
      ]

fb_base_url = 'https://m.facebook.com/'
first_page_error = []
for fb in FB:
    print("***********************************", fb, "***********************************")
    links = []
    folder = f"/home/amir/DATA/{fb}"
    os.mkdir(folder)
    time.sleep(4)
    complted_url = fb_base_url + fb
    try:
        browser.get(complted_url)
        s_Main_page = BeautifulSoup(browser.page_source, "lxml")

        for i in s_Main_page.select("div", {"class" : "cs g ch"}):
            try:
                link = i.find("a")['href']
                if link.startswith(f"/{fb}?v=timeline&lst="):
                    timeline_LINK = "https://mobile.facebook.com" + link
            except:
                pass
        try:
            timeline_LINK
        except:
            try:
                s_Main_page.find("div", {"class" : "dh f cw"})
                for i in s_Main_page.find("div", {"class" : "dh f cw"}).select("a"):
                    if i.text == "Timeline":
                        timeline_LINK = "https://m.facebook.com" + i['href']
            except:
                pass
                print(f"{fb}: No timeline Link")
                continue

        browser.get(timeline_LINK)
        del timeline_LINK
        s_first_page = BeautifulSoup(browser.page_source, "lxml")
        file_name = f"{folder}/0_{fb}.pkl"
        with open(file_name, "wb") as file:
            pickle.dump(str(s_first_page), file)
        try:
            next_page_link = "https://mobile.facebook.com" + s_first_page.find("div", {"id" : "u_0_2"}).find("a")['href']
        except:
            next_page_link = "https://mobile.facebook.com" + s_first_page.find("div", {"id" : "u_0_3"}).find("a")['href']
        c = 1
        while True:
            time.sleep(2)
            c += 1
            try:
                next_page_link = next_page(next_page_link, c, fb)
            except:
                print("end of posts")
                break
    except:
        first_page_error.append(fb)
        print(fb, "First page Error")
    if links:
        name = f"{folder}/LINK_pages_5_posts_in_each_page_{fb}.pkl"
        with open(name, "wb") as file:
            pickle.dump(links, file)
        os.system("firefox " + links[-1])
    else:
        print(fb, "There is no link")