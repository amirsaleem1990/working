import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
import datetime
from login import LOGIN
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

browser = LOGIN()
pages i nedd in list: "idreesazad2", "itsfoss/", "azeemnama", "AkxOAwaz"
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
		mmz.append(s)
		for i in s.select("a"):
			try:
				link = i['href']
				if (link.startswith("/" + fb + "/posts/")) and (not link in str(all_links)) and (not "?comment_id=" in link) and (not link in all_links[fb]):
					link = "https://www.facebook.com" + link
					all_links[fb].append((link, str(now)))
					links_to_open.append(link)
					browser.get(link)
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
				pass
	c += 1
	perc = counter/len(FB)*100
	print("{:3} {} %  || {:2} of {}  ||  ".format(int(perc), " ", counter, len(FB)),current_time(),f" ||  {c} links in {fb}")

# browser.close()

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

# os.system("ipython3 /home/amir/github/working/Facebook_posts_links/last_post.py")