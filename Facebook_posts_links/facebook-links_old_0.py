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

def write_to_file(link, post):
	global succussfully_extracted
	file = open(file_name, "a+")
	file.write("\n" + "#"*30 + "\n")
	file.write(link + "\n")
	file.write(post + "\n")
	file.close()
	succussfully_extracted += 1


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

with open("All_FB_links_names_corrected.pkl", "rb") as file:
	all_links = pickle.load(file)

stored_links_qty = sum([len(all_links[i]) for i in all_links])	

with open("/home/amir/github/Amir-personal/facebook-userName-and-password_3.txt", "r") as file:
	usrname, pas = file.read().splitlines()

print("Attempting to Login   ", current_time())
Successfully_logedin = True
Successfully_logedin_num = 0
# if input("Are u need visual tracking? [y\\n]:\t").lower() == "y":
	# visual = True
# else:
from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")
visual = False
	
while Successfully_logedin:
	Successfully_logedin_num += 1
	if Successfully_logedin_num > 1:
		print(f"Attempt no. {Successfully_logedin_num} to Login")
	try:
		if visual:
			browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver")
		else:
			browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)	

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
		Successfully_logedin = False
	except:
		pass
# pages i nedd in list: "idreesazad2", "itsfoss/", "azeemnama", "AkxOAwaz"
FB = [i.split("\t")[0].strip() for i in open("/home/amir/github/working/Facebook_posts_links/FB.txt", "r").read().splitlines()]

with open("ids_removed_from_facebook.pkl", "rb") as file:
    ids_removed_from_facebook = pickle.load(file)
ids_removed_from_facebook = list(ids_removed_from_facebook.keys())

fb_base_url = "https://web.facebook.com/"
extrected_links = []
new_links = []
counter = 0
links_to_open = []

now = datetime.datetime.now()
mmz = []
errors = []

succussfully_extracted = 0
for fb in FB:
	c = 0
	counter += 1
	if not fb in ids_removed_from_facebook:
		complted_url = fb_base_url + fb
		if not fb in all_links:
			print(f"new id added: <{fb_base_url + fb}>")
			all_links[fb] = []
		browser.get(complted_url)
		s = BeautifulSoup(browser.page_source, "lxml")

		##################################################
		# only for groups 
		if fb.startswith("groups"):
			for i in s.select("a"):
				try:
					link = i['href']
					if link.startswith(f"/{fb}permalink/"):
						link = "https://web.facebook.com" + link
						# print("a", end="|")
						if not link in str(all_links):
							# print("b", end="|")
							all_links[fb].append((link, str(now)))
							links_to_open.append(link)
							try:
								browser.get(link)
								# print("c", end="|")
								post = BeautifulSoup(browser.page_source, features="lxml").find("div", {"data-testid" : "post_message"}).text.replace("<br/>", "\n")
								# print("d", end="|")
								if post:
									file_name = f"{fb.strip('/').split('/')[1]}.txt"
									write_to_file(file_name, link, post)
							except:
								errors.append([fb, link])
				except:
					pass
		##################################################	
		else:
			a = s.find("div", {"id" : "timeline_story_column"})
			mmz.append(a)
			try:
				links_ = a.select('a')
				for i in links_:
					link = i['href']
					if (link.startswith("https://www.facebook.com/")) or (link.startswith("https://web.facebook.com/")):
						if not link in str(all_links):
							if "/posts/" in link: # failing to capture like this link (https://web.facebook.com/permalink.php?story_fbid=129882195152447&id=100043920022318)
								if not "?comment_id=" in link:
									all_links[fb].append((link, str(now)))
									links_to_open.append(link)
									c += 1
									try:
										browser.get(link)
									except:
										errors.append([fb, link])
										continue
									soup = BeautifulSoup(browser.page_source, "lxml")
									try:
										aa = soup.find("div", {"class" : "_5wj-"}).text
										if len(aa) > 0:
											file_name = f"{fb}.txt"
											write_to_file(file_name, link, aa)
										else:
											errors.append([fb, link])
									except:
										errors.append([fb, link])
										pass

			except:
				continue
	perc = counter/len(FB)*100
	print("{:3} {} %  || {:2} of {}  ||  ".format(int(perc), " ", counter, len(FB)),current_time(),f" ||  {c} links in {fb}")

browser.close()

if not links_to_open:
	if "check" in os.listdir():
		import shutil
		shutil.rmtree("check", ignore_errors=False)
	os.mkdir("check")
	os.chdir("check/")
	for e, i in enumerate(mmz):
		with open(str(e) + ".txt", "w") as file:
			file.write(str(i))
	from termcolor import colored
	print(colored("\n\n<check> folder created, you can check there why you not get any link\n\n", 'red'))


links_qty_after_addition = sum([len(all_links[i]) for i in all_links])


procecced = 0
if succussfully_extracted:
	print("New links Qty: ", links_qty_after_addition - stored_links_qty)
	print("\n\nsuccussfully extracted: ", succussfully_extracted)
	with open("All_FB_links_names_corrected.pkl", "wb") as file:
		pickle.dump(all_links, file)

	for i in links_to_open:
		procecced += 1
		os.popen("firefox " + i)
		
		if procecced > 20:
			input("\n\nPress Enter\n\n")
			procecced = 0
else:
	with open("errors.txt", "w") as file:
		for error in errors:
			file.write(error[0] + ":  " + error[1] + "\n")
	print(f"""\n\nNo link was extracted succussfully, you can need bug fixing we saved all the scrapped data at: 
		/home/amir/github/working/Facebook_posts_links/check/ \n\n""")


try:
	os.remove("geckodriver.log")
except:
	pass

os.system("ipython3 /home/amir/github/working/Facebook_posts_links/last_post.py")

# import os
# import time
# import pickle
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import numpy as np
# import time
# import datetime
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.add_argument("--headless")

# os.chdir("/home/amir/github/working/Facebook_posts_links/")

# os.system("clear")

# def current_time():
# 	n = datetime.datetime.now()
# 	t = ':'.join([str(i) for i in [n.hour, n.minute, n.second]])
# 	tt = ""
# 	for i in t.split(":"):
# 		if len(i) == 1:
# 			tt += "0" + i
# 		else:
# 			tt += i
# 		tt += ":"
# 	tt = tt.strip(":")
# 	return tt

# # home = list(os.popen("echo $HOME"))[0].strip()
# # # in kali the symbolic linc of <github> folder is at </root/amir>
# # if home == "/root":
# # 	home = "/root/amir"

# with open("All_FB_links_names_corrected.pkl", "rb") as file:
# 	all_links = pickle.load(file)

# stored_links_qty = sum([len(all_links[i]) for i in all_links])	

# with open("/home/amir/github/Amir-personal/facebook-userName-and-password.txt", "r") as file:
# 	usrname, pas = file.read().splitlines()

# print("Attempting to Login", current_time())

# Successfully_logedin = True
# while Successfully_logedin:
# 	try:
# 		# browser = webdriver.Firefox(executable_path=home + "/github/working/Facebook_posts_links/geckodriver")
# 		browser = webdriver.Firefox(executable_path = "/home/amir/github/working/Facebook_posts_links/geckodriver", options=options)
# 		#navigates you to the facebook page.
# 		browser.get('https://www.facebook.com/')

# 		#find the username field and enter the email example@yahoo.com.
# 		time.sleep(np.random.randint(3, 6))
# 		username = browser.find_elements_by_css_selector("input[name=email]")
# 		username[0].send_keys(usrname)


# 		#find the password field and enter the password password.
# 		time.sleep(np.random.randint(3, 6))
# 		password = browser.find_elements_by_css_selector("input[name=pass]")
# 		password[0].send_keys(pas)


# 		#find the login button and click it.
# 		time.sleep(np.random.randint(3, 6))
# 		loginButton = browser.find_elements_by_css_selector("input[type=submit]")
# 		loginButton[0].click()
# 		print("Successfully Logged in", current_time())
# 		Successfully_logedin = False
# 	except:
# 		pass
# # pages i nedd in list: "idreesazad2", "itsfoss/", "azeemnama"

# # names = ["Mushtaq", "Asif mehmood", "Zahid mughal", "Mohammad Fahad Haris", "Abdullah Adam", "Hm Zubair", "Muhammad Imran", "Munib Hussain", "Jameel Baloch",
# # 	 "Rizwan Asad Khan", "Abubakr Quddusi", "Mohammad Din Jauhar", "Riayatullah Farooqui", "Asim AllahBakhsh", "Sohaib naseem", "Idrees Aazad", 
# # 	 "Abu muhammad musab", "Mahtab khan", "mohammad.saleem"]
# FB = ["MMushtaqYusufzai", 					# Muhammad Mushtaq
# 		"asif.mahmood.1671", 				# asif mahmood
# 		"zahid.mughal.5895", 				# zahid mughal
# 		"mohammad.f.haris", 				# mohammad fahad haris
# 		"abdullah.adam49", 					# abdullah adam 
# 		"hm.zubair.52", 					# Hm Zubair 
# 		"abumaryam82",  					# Muhammad Imran (Blocked)
# 		"yaldrim.khalid.9", 				# Muhammad Imran
# 		"munib.hussain86", 					# munib hussain 
# 		"jameelbaloch1924", 				# jameel baloch 
# 		"theguided1",  						# Rizwan Asad Khan
# 		"abubakr.quddusi.3", 				# abubakr quddusi 
# 		"mohammaddin.jauhar.7", 			# mohammad din jauhar 
# 		"Riayat.Farooqui",  				# riayatullah farooqui 
# 		"asim.allahbakhsh", 				# asim allahbakhsh 
# 		"sohaib.naseem.3", 					# صہیب نسیم‎  
# 		"idreesazaad", 						# Idrees Azad ‎
# 		"Abu.Musab.98622733", 				# ابو محمد مصعب 
# 		"profile.php?id=100026041448813", 
# 		"mohammad.saleem.568847", 			# mohammad saleem 
# 		"hammad.sarwar.9400",
# 		"profile.php?id=100043920022318",   # سرورالدین سرور
# 		"ajeebscenehaibhai", 
# 		"nouman.atd.3", 					# Nouman Ihsan
# 		"profile.php?id=100032249983289", 	# انس اسلام
# 		"HamidKamaluddin.personal", 		# Hamid kamaluddin
# 		"faisal.shahzad.1253236", 			# محمد فیصل شہزاد
# 		"tariq.habib.969952", 				# tariq habib
# 		"mahtabaziz", 						# mahtab khan
# 		"suhaib.jamal.1" 					# Suhaib Jamal
# 	  ]





# fb_base_url = "https://web.facebook.com/"
# extrected_links = []
# new_links = []
# counter = 0
# links_to_open = []

# now = datetime.datetime.now()
# mmz = []
# errors = []
# ids_removed_from_facebook = ["abumaryam82", "hammad.sarwar.9400"]
# succussfully_extracted = 0
# for fb in FB:
# 	c = 0
# 	counter += 1
# 	if not fb in ids_removed_from_facebook:
# 		complted_url = fb_base_url + fb
# 		if not fb in all_links:
# 			print(f"new id added: <{fb_base_url + fb}>")
# 			all_links[fb] = []
# 		browser.get(complted_url)
# 		s = BeautifulSoup(browser.page_source, "lxml")
# 		a = s.find("div", {"id" : "timeline_story_column"})
# 		mmz.append(a)
# 		try:
# 			links_ = a.select('a')
# 			for i in links_:
# 				link = i['href']
# 				if link.startswith("https://web.facebook.com/"):
# 					if not link in str(all_links):
# 						if "/posts/" in link:
# 							if not "?comment_id=" in link:
# 								all_links[fb].append((link, str(now)))
# 								links_to_open.append(link)
# 								c += 1
# 								try:
# 									browser.get(link)
# 								except:
# 									errors.append([fb, link])
# 									continue
# 								soup = BeautifulSoup(browser.page_source, "lxml")
# 								try:
# 									aa = soup.find("div", {"class" : "_5wj-"}).text
# 									if len(aa) > 0:
# 										file_name = f"{fb}.txt"
# 										file = open(file_name, "a+")
# 										file.write("\n" + "#"*30 + "\n")
# 										file.write(link + "\n")
# 										file.write(aa + "\n")
# 										succussfully_extracted += 1
# 										file.close()
# 									else:
# 										errors.append([fb, link])
# 								except:
# 									errors.append([fb, link])
# 									pass

# 		except:
# 			continue
# 	perc = counter/len(FB)*100
# 	print("{:3} {} %  || {:2} of {}  ||  ".format(int(perc), " ", counter, len(FB)),
# 						 current_time(),
# 						 f" ||  {c} links in {fb}")
# 	if not c:
# 		print(complted_url)
# 		print("****************************************************************************")

# browser.close()

# if not links_to_open:
# 	if "check" in os.listdir():
# 		import shutil
# 		shutil.rmtree("check", ignore_errors=False)
# 	os.mkdir("check")
# 	os.chdir("check/")
# 	for e, i in enumerate(mmz):
# 		with open(str(e) + ".txt", "w") as file:
# 			file.write(str(i))
# 	from termcolor import colored
# 	print(colored("\n\n<check> folder created, you can check there why you not get any link\n\n", 'red'))


# links_qty_after_addition = sum([len(all_links[i]) for i in all_links])

# if succussfully_extracted:
# 	print("New links Qty: ", links_qty_after_addition - stored_links_qty)
# 	print("\n\nsuccussfully extracted: ", succussfully_extracted)
# 	with open("All_FB_links_names_corrected.pkl", "wb") as file:
# 		pickle.dump(all_links, file)
# 	for i in links_to_open:
# 		os.popen("firefox " + i)

# else:
# 	with open("errors.txt", "w") as file:
# 		for error in errors:
# 			file.write(error[0] + ":  " + error[1] + "\n")
# 	print(f"\n\nThere is {len(errors)} errors, saved in <errors.txt>\n\n")


# try:
# 	os.remove("geckodriver.log")
# except:
# 	pass