def open_links():
	import pandas as pd
	import os
	import pickle
	import itertools
	import datetime

	# read all fresh links
	with open("/home/amir/github/working/Facebook_posts_links/current_data.pkl", "rb") as file:
	    current_data = pickle.load(file)
	# remove all keys that have no values[empty lists]
	current_data = {k:y for k,y in current_data.items() if current_data[k]}

	# read master data, that contain all scraped links ever
	master_csv = pd.read_csv("/home/amir/github/working/Facebook_posts_links/links.csv")

	# remove all links from <current_data> that exists in <master_csv> file
	for k,v in current_data.items():
	    for value in v:
	        if value in master_csv['link']:
	            current_data[k].remove(value)

	# lsit of all fresh links
	all_current_dict_links = list(itertools.chain(*current_data.values()))
	# open all links in firefox browser
	for link in all_current_dict_links:
			os.system("firefox " + link)        

	# current date and time 
	DateTime = str(datetime.datetime.now())
	fresh_df = pd.DataFrame()

	# now we create dataframe for fresh data
	dd = {}
	for i in current_data:
	    dd[i] = [(v, str(DateTime)) for v in current_data[i]]
	for i in dd:
	    adf =  pd.DataFrame(dd[i])
	    adf['Name'] = i
	    fresh_df = fresh_df.append(adf)

	# append fresh dataframe to master dataframe and save it
	if len(fresh_df) > 0:
	    fresh_df.columns = ["link", "Date", "Name"]
	    new_and_old = pd.concat([master_csv, fresh_df])
	    new_and_old.to_csv("master_csv", index = False)
