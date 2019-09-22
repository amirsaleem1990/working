import os
import pickle
import itertools

with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "rb") as file:
    current_data = pickle.load(file)
current_data = {k:y for k,y in link_dict.items() if current_data[k]}

with open("/home/amir/github/working/Facebook_posts_links/All_FB_links.pkl", "rb") as file:
    all_links = pickle.load(file)


all_current_dict_links = list(itertools.chain(*current_data.values()))
all_all_links_dict_links = list(itertools.chain(*all_links.values()))

for link in all_current_dict_links:
	if not link in all_all_links_dict_links:
		os.system("firefox " + link)        


for k,v in current_data.items():
    if not k in all_links:
        all_links[k] = v
    else:
        for i in v:
            if not i in all_links[k]:
                all_links[k].append(i)


with open("/home/amir/github/working/Facebook_posts_links/All_FB_links.pkl", "wb") as file:
	pickle.dump(all_links, file)