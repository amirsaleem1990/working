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

os.chdir("/home/amir/github/working/Facebook_posts_links/")

os.system("clear")

def current_time():
	n = datetime.datetime.now()
	t = ':'.join([str(i) for i in [n.hour % 12, n.minute, n.second]])
	tt = ""
	for i in t.split(":"):
		if len(i) == 1:
			tt += "0" + i
		else:
			tt += i
		tt += ":"
	tt = tt.strip(":")
	return tt

# home = list(os.popen("echo $HOME"))[0].strip()
# # in kali the symbolic linc of <github> folder is at </root/amir>
# if home == "/root":
# 	home = "/root/amir"

FB = ["MMushtaqYusufzai", 					# Muhammad Mushtaq
		"asif.mahmood.1671", 				# asif mahmood
		"zahid.mughal.5895", 				# zahid mughal
		"mohammad.f.haris", 				# mohammad fahad haris
		"abdullah.adam49", 					# abdullah adam 
		"hm.zubair.52", 					# Hm Zubair 
		"muhammad.imra.100",				# Muhammad Imran
		"munib.hussain86", 					# munib hussain 
		"jameelbaloch1924", 				# jameel baloch           #Blocked
		"theguided1",  						# Rizwan Asad Khan
		"abubakr.quddusi.3", 				# abubakr quddusi 
		"mohammaddin.jauhar.7", 			# mohammad din jauhar 
		"Riayat.Farooqui",  				# riayatullah farooqui 
		"asim.allahbakhsh", 				# asim allahbakhsh 
		"sohaib.naseem.3", 					# میسن بیہص  
		"idreesazaad", 						# Idrees Azad ‎
		"Abu.Musab.98622733", 				# بعصم دمحم وبا 
		"profile.php?id=100026041448813", 
		"profile.php?id=100010667655748",   # mohammad saleem 
		"profile.php?id=100043920022318",   # سرورالدین سرور
		"ajeebscenehaibhai", 
		"nouman.atd.3", 					# Nouman Ihsan
		"profile.php?id=100032249983289", 	# مالسا سنا              (Blocked)
		"anas.islam.3551",                  # مالسا سنا
		"HamidKamaluddin.personal", 		# Hamid kamaluddin
		"faisal.shahzad.1253236", 			# دازہش لصیف دمحم
		"tariq.habib.969952", 				# tariq habib
		"mahtabaziz", 						# mahtab khan
		"suhaib.jamal.1", 					# Suhaib Jamal
		"hanifsamanaa",						# hanif samanaa
		"groups/pakdotai/",					# pakistan.ai
		"atheismcrusher.pk", 				# abu ibrahim
		"roxane.apolonio.773",				# کاڑھک اد ےکاک 
		"anwaar456",						# ردیح راونا
		"muhammad.bhatti.9250",				# Muhammad Bhatti
		"Bhaihasib1",						# Haseeb Khan
		"mateen.ahmad2010",					# Syed Mateen Ahmad
		"profile.php?id=100009666136877",	# Faizullah Khan
		"profile.php?id=100004721416966",	# Dr-Muhammad Shahbaz Manj
		"profile.php?id=100010345081577",	# Ali Imran
		"zeeshan1857",						# Zeeshan Waraich
		"jamilasgharjaami"					# jamil asghar jaami 
	  ]

with open("All_FB_links_names_corrected.pkl", "rb") as file:
	all_links = pickle.load(file)

stored_links_qty = sum([len(all_links[i]) for i in all_links])	

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()

print("Attempting to Login   ", current_time())
Successfully_logedin = True
Successfully_logedin_num = 0
fb_base_url = "https://m.facebook.com/" # "https://web.facebook.com/"
while Successfully_logedin:
	Successfully_logedin_num += 1
	if Successfully_logedin_num > 1:
		print(f"Attempt no. {Successfully_logedin_num} to Login")
	try:
		browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver")
		
		#navigates you to the facebook page.
		browser.get(fb_base_url)

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
		okButton = browser.find_elements_by_css_selector("input[type=submit]")
		okButton[0].click()

		print("Successfully Logged in", current_time())
		Successfully_logedin = False
	except:
		pass
    

with open("ids_removed_from_facebook.pkl", "rb") as file:
	ids_removed_from_facebook = pickle.load(file)
ids_removed_from_facebook = list(ids_removed_from_facebook.keys())


extrected_links = []
new_links = []
counter = 0
links_to_open = []

now = datetime.datetime.now()
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
        with open(f"{folder_name}/{len(pages_links)}_{fb}.pkl", "wb") as file:
            to_save = str(s)
            pickle.dump(to_save, file)
    except:
        print("ERROR: ",fb, LINK)
        import sys
        sys.exit()


for fb in FB:
    try:
        print(fb)
        folder_name = "/home/amir/PKL/" + fb
        os.mkdir(folder_name)
        complted_url = fb_base_url + fb

        try:
            browser.get(complted_url)
        except:
            print("ID not found", fb)
            import sys
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
        with open(f"{folder_name}/LINKS.pkl", "wb") as file:
            pickle.dump(pages_links, file)
    except:
        print("Error in: ", fb)
        pass