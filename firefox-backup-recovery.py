import sys 
import pathlib 
import lz4.block 
import json 
import pandas as pd 
import sys

try:
	folder_name = sys.argv[1]
except:
	folder_name = input("Enter folder name: ")
to_be_exclude = ['https://stackoverflow.com/questions/tagged/bash+linux']


 
# file_name = list(pathlib.Path.home().joinpath('.mozilla/firefox').glob('*default*/sessionstore-backups/recovery.js*'))[0]
# file_name = '/' + '/'.join(file_name.parts).lstrip("/")
# file_name = '/home/amir/.firefox_backups/07-24-21_17:30:48/recovery.jsonlz4'
file_name = folder_name + '/recovery.jsonlz4'

# file = pathlib.Path.home().joinpath('.mozilla/firefox').glob('*default*/sessionstore-backups/recovery.js*') 
# b_ = list(file)[0].read_bytes() 
b_ = open(file_name, 'rb').read()

if b_[:8] == b'mozLz40\x00': 
	b = lz4.block.decompress(b_[8:])
	tabs = json.loads(b)['windows'][0]['tabs']
	bef=len(str(tabs))
	for tab in tabs:
		tab_ = tab['entries']
		lst = []
		for e, entry in enumerate(tab_):
			if entry['url'] in to_be_exclude:
				del tab_[e]
				print("---------------Excluded")
				pass
		# tab[e] = lst
	# aft=len(str(tabs))
	# print(bef, aft)
# j = json.loads(b)
# j['windows'][0]['tabs'] = tabs
# bytes_ = b_[:8] + bytes(str(j), encoding="raw_unicode_escape")
# compressed = lz4.block.compress()
# file = pathlib.Path.home().joinpath('.mozilla/firefox').glob('*default*/sessionstore-backups/recovery.js*')
# list(file)[0].write_bytes(compressed)
# # open(file_name, 'wb').write(compressed)
# sys.exit()

df = pd.DataFrame(json.loads(b)['windows'][0]['tabs']) 

x = json.loads(b)['windows'][0]['tabs'] 

lst = [] 
for i in x: 
	entries = i['entries'] 
	for i_dict in entries: ## 
		lst.append([i_dict['url'], i_dict['title'], i_dict['ID']]) 

from IPython.display import display
pd.set_option('display.max_rows', 200)
# pd.set_option('display.max_columns', 8)
# pd.set_option('display.max_colwidth', 200)
df = (
	pd.DataFrame(lst, columns=['url', 'title', 'ID'])
	.drop_duplicates(subset=["ID", "url"])
	.sort_values("ID")
	.drop_duplicates(subset="ID", keep="last").sort_values("url")
	)
display(
	df
	.url
	.str
	.split("//", 1)
	.str[1]
	.str
	.replace("^www.", "")
	.str
	.split(".", 1)
	.str[0]
	.value_counts()
	.rename("Count")
	.rename_axis("Website")
	.reset_index()
	)

# print("\n\n\n")

# display(df)
import os
df.to_csv("/home/amir/.browser_df.csv", index=False)
os.system("gopen /home/amir/.browser_df.csv")
# print("\n")

