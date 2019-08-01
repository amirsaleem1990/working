import time
import pickle
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys
with open("All_FB_links.pkl", "rb") as file:
    all_links = pickle.load(file)
    
with open("../../Amir-personal/facebook-userName-and-password.txt", "r") as file:
	usrname, pas = file.read().splitlines()
    
browser = webdriver.Firefox(executable_path="./geckodriver")
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
for name, url in zip(["Mushtaq", "Asif mehmood", "Zahid mughal", "Mohammad Fahad Haris", "Abdullah Adam", "Hm Zubair", "Muhammad Imran", "Munib Hussain", "Jameel Baloch",
                     "Rizwan Asad Khan", "Abubakr Quddusi", "Mohammad Din Jauhar", "Riayatullah Farooqui", "Asim AllahBakhsh", "Sohaib naseem", "Idrees Aazad", 
                     "Abu muhammad musab", "Mahtab khan"], 
                     ["https://web.facebook.com/MMushtaqYusufzai", "https://web.facebook.com/asif.mahmood.1671", "https://web.facebook.com/zahid.mughal.5895", 
                     "https://web.facebook.com/mohammad.f.haris", "https://web.facebook.com/abdullah.adam49", "https://web.facebook.com/hm.zubair.52", 
                      "https://web.facebook.com/abumaryam82", "https://web.facebook.com/munib.hussain86", "https://web.facebook.com/jameelbaloch1924", 
                      "https://web.facebook.com/theguided1", "https://web.facebook.com/abubakr.quddusi.3",
                     "https://web.facebook.com/mohammaddin.jauhar.7", "https://web.facebook.com/Riayat.Farooqui", "https://web.facebook.com/asim.allahbakhsh",
                     "https://web.facebook.com/sohaib.naseem.3", "https://web.facebook.com/idreesazaad", "https://web.facebook.com/Abu.Musab.98622733", 
                     "https://web.facebook.com/profile.php?id=100026041448813"]):
    if not name in link_dict:
        link_dict[name] = []
    browser.get(url)
    s = BeautifulSoup(browser.page_source, "lxml")
    a = s.find("div", {"id" : "timeline_story_column"})
    for i in a.find_all('a'):
        try:
            if i['href'].startswith(url + "/post"):
                if not i['href'] in all_links[name]:
                    link_dict[name].append(i['href'])
        except:
            pass

                             
for name,list_of_links in link_dict.items():
    lst = []
    for link in list_of_links:
        if not "comment_id" in link:
            lst.append(link)
    link_dict[name] = lst

with open("current_data.pkl", "wb") as file:
    pickle.dump(link_dict, file)

time.sleep(10)
browser.close()