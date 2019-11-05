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
	print(tt)

home = list(os.popen("echo $HOME"))[0].strip()
# in kali the symbolic linc of <github> folder is at </root/amir>
if home == "/root":
	home = "/root/amir"

with open(home + "/github/working/Facebook_posts_links/All_FB_links_names_corrected.pkl", "rb") as file:
    all_links = pickle.load(file)

stored_links_qty = sum([len(all_links[i]) for i in all_links])    

with open(home + "/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
    usrname, pas = file.read().splitlines()
n = datetime.datetime.now()
print("Attempting to Login", current_time())

# browser = webdriver.Firefox(executable_path=home + "/github/working/Facebook_posts_links/geckodriver")
browser = webdriver.Firefox(executable_path= home + "/github/working/Facebook_posts_links/geckodriver", options=options)
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
print("Successfully Logged in", current_time())

# pages i nedd in list: "idreesazad2", "itsfoss/"

# names = ["Mushtaq", "Asif mehmood", "Zahid mughal", "Mohammad Fahad Haris", "Abdullah Adam", "Hm Zubair", "Muhammad Imran", "Munib Hussain", "Jameel Baloch",
# 	 "Rizwan Asad Khan", "Abubakr Quddusi", "Mohammad Din Jauhar", "Riayatullah Farooqui", "Asim AllahBakhsh", "Sohaib naseem", "Idrees Aazad", 
# 	 "Abu muhammad musab", "Mahtab khan", "mohammad.saleem"]
FB = ["MMushtaqYusufzai", "asif.mahmood.1671", "zahid.mughal.5895", 
     "mohammad.f.haris", "abdullah.adam49", "hm.zubair.52", 
      "abumaryam82", "munib.hussain86", "jameelbaloch1924", 
      "theguided1", "abubakr.quddusi.3",
     "mohammaddin.jauhar.7", "Riayat.Farooqui", "asim.allahbakhsh",
     "sohaib.naseem.3", "idreesazaad", "Abu.Musab.98622733", 
     "profile.php?id=100026041448813", "mohammad.saleem.568847", "hammad.sarwar.9400",
     "ajeebscenehaibhai"]

fb_base_url = "https://web.facebook.com/"
extrected_links = []
new_links = []
counter = 0
links_to_open = []
for fb in FB:
	c = 0
	counter += 1
	n = datetime.datetime.now()
	complted_url = fb_base_url + fb
	if not fb in all_links:
		print(f"new id added: <{fb_base_url + fb}>")
		all_links[fb] = []
	browser.get(complted_url)
	s = BeautifulSoup(browser.page_source, "lxml")
	a = s.find("div", {"id" : "timeline_story_column"})
	try:
		links_ = a.select('a')
		for i in links_:
			link = i['href']
			if "/posts/" in link:
				if link.startswith("https://web.facebook.com/"):
					if not "?comment_id=" in link:
						if not link in str(all_links):
							all_links[fb].append((link, str(now)))
							links_to_open.append(link)
							c += 1

	except:
		pass
	perc = counter/len(FB)*100
	print("{} {:5} %  || {} of {}  ||  ".format(int(), " ", counter, len(FB)),
						 current_time(),
						 f" ||  {c} links in {fb}")
links_qty_after_addition = sum([len(all_links[i]) for i in all_links])

print("New links Qty: ", links_qty_after_addition - stored_links_qty)

with open(home + "/github/working/Facebook_posts_links/All_FB_links_names_corrected.pkl", "wb") as file:
	pickle.dump(all_links, file)
browser.close()
os.remove("geckodriver.log")

for i in links_to_open:
	os.popen("firefox " + i)