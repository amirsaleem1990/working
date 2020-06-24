#!/usr/bin/python3
import pickle
import os
file_ = "/home/amir/github/working/Facebook_posts_links/links_to_open.pkl"
links_to_open = pickle.load(open(file_, "rb"))
print(f"There is {len(links_to_open)} in the file\n")
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
if not links_to_open:
	print("All links opened\n")
else:
	print(f"There are still {len(links_to_open)} links to open in the file\n")
pickle.dump(links_to_open, open(file_, "wb"))