#!/usr/bin/python3
import pickle
import os
file_ = "/home/amir/github/working/Facebook_posts_links/links_to_open.pkl"
links_to_open = pickle.load(open(file_, "rb"))
procecced = 0
links_opened = []
for i in links_to_open:
	procecced += 1
	os.popen("firefox " + i)
	links_opened.append(i)
	if procecced > 20:
		ans = input("\nPress Enter for procecced, for EXIT Enter q\n")
		if ans == 'q':
			break
		else:
			procecced = 0
links_to_open = [i for i in links_to_open if not i in links_opened]
pickle.dump(links_to_open, open(file_, "wb")