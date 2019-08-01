import os
import pickle
import itertools

with open("current_data.pkl", "rb") as file:
    current_data = pickle.load(file)

with open("All_FB_links.pkl", "rb") as file:
    all_links = pickle.load(file)


all_current_dict_links = list(itertools.chain(*current_data.values()))
all_all_links_dict_links = list(itertools.chain(*all_links.values()))

for links_list in current_data.values():
    for link in links_list:
    	if not link in all_current_dict_links:
	        # os.system("firefox "+  link)
	        pass
        


for k,v in current_data.items():
    if not k in all_links:
        all_links[k] = v
    else:
        for i in v:
            if not i in all_links[k]:
                all_links[k].append(i)


with open("All_FB_links.pkl", "wb") as file:
	pickle.dump(all_links, file)