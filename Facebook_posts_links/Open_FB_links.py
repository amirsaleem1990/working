import pandas as pd
import os
import pickle
import itertools
import datetime

with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "rb") as file:
    current_data = pickle.load(file)
current_data = {k:y for k,y in current_data.items() if current_data[k]}

master_csv = pd.read_csv("/home/amir/github/working/Facebook_posts_links/links.csv")
all_all_links_dict_links = master_csv.link.values

# remove all links from <current_data> that exists in <master_csv> file
for k,v in current_data.items():
    for value in v:
        if value in all_all_links_dict_links:
            current_data[k].remove(value)

all_current_dict_links = list(itertools.chain(*current_data.values()))
for link in all_current_dict_links:
		os.system("firefox " + link)        



DateTime = str(datetime.datetime.now())
fresh_df = pd.DataFrame()
dd = {}
for i in link_dict:
    if link_dict[i]:
        dd[i] = [(v, str(DateTime)) for v in link_dict[i]]
for i in dd:
    adf =  pd.DataFrame(dd[i])
    adf['Name'] = i
    fresh_df = fresh_df.append(adf)

if len(fresh_df) > 0:
    fresh_df.columns = ["link", "Date", "Name"]
    new_and_old = pd.concat([master_csv, fresh_df])
    new_and_old.to_csv("master_csv", index = False)
