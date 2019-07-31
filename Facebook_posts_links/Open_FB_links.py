import os
import pickle

with open("current_data.pkl", "rb") as file:
    current_data = pickle.load(file)


# for links_list in current_data.values():
#     for link in links_list:
#         os.system("firefox "+  link)
        
with open("All_FB_links.pkl", "rb") as file:
    all_links = pickle.load(file)

for k,v in current_data.items():
    if not k in all_links:
        all_links[k] = v
    else:
        for i in v:
            if not i in all_links[k]:
                all_links[k].append(i)


with open("All_FB_links.pkl", "wb") as file:
	pickle.dump(all_links, file)