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
DateTime = str(datetime.datetime.now())
# with open("/home/amir/github/working/Facebook_posts_links/All_FB_links.pkl", "rb") as file:
#     all_links = pickle.load(file)

master_csv = pd.read_csv("/home/amir/github/working/Facebook_posts_links/links.csv")
    
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
for name, url in zip(
    ["Mushtaq", "Asif mehmood", "Zahid mughal", "Mohammad Fahad Haris", "Abdullah Adam", "Hm Zubair", "Muhammad Imran", "Munib Hussain", "Jameel Baloch",
	 "Rizwan Asad Khan", "Abubakr Quddusi", "Mohammad Din Jauhar", "Riayatullah Farooqui", "Asim AllahBakhsh", "Sohaib naseem", "Idrees Aazad", 
	 "Abu muhammad musab", "Mahtab khan", "mohammad.saleem"], 
     ["MMushtaqYusufzai", "asif.mahmood.1671", "zahid.mughal.5895", 
     "mohammad.f.haris", "abdullah.adam49", "hm.zubair.52", 
      "abumaryam82", "munib.hussain86", "jameelbaloch1924", 
      "theguided1", "abubakr.quddusi.3",
     "mohammaddin.jauhar.7", "Riayat.Farooqui", "asim.allahbakhsh",
     "sohaib.naseem.3", "idreesazaad", "Abu.Musab.98622733", 
     "profile.php?id=100026041448813", "mohammad.saleem.568847"]):
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

fresh_df = pd.DataFrame()
dd = {}
for i in link_dict:
    if link_dict[i]:
        dd[i] = [(v, "before 20-sep-2019") for v in link_dict[i]]
for i in dd:
    adf =  pd.DataFrame(dd[i])
    adf['Name'] = i
    fresh_df = fresh_df.append(adf)

if len(fresh_df) > 0:
    fresh_df.columns = ["link", "Date", "Name"]
    new_and_old = pd.concat([master_csv, fresh_df])
    new_and_old.to_csv("master_csv", index = False)
# with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "wb") as file:
#     pickle.dump(link_dict, file)

# browser.close()
# os.remove("geckodriver.log")