# see days since last post 
from tabulate import tabulate
import os
import pandas as pd
import pickle
import datetime
os.chdir("/home/amir/github/working/Facebook_posts_links/")
os.system("ipython3 links-pickle-to-df.py")

with open("ids_removed_from_facebook.pkl", "rb") as file:
    ids_removed_from_facebook = pickle.load(file)
ids_removed_from_facebook = list(ids_removed_from_facebook.keys())

previos_data = pd.read_csv("All_FB_links_names_corrected.csv")
crnt_time = pd.to_datetime(
	datetime.datetime.now(),
	infer_datetime_format=True)

diff = []
for fb in  previos_data.Name.unique():
    last_date = pd.to_datetime(
        previos_data[previos_data.Name == fb].tail(1).Tate.values,
        infer_datetime_format=True)
    diff.append(str(list((crnt_time - last_date))[0]).split()[0])
    
df_diff = pd.DataFrame([previos_data.Name.unique(), diff]).T
df_diff.columns = ["Name", "No post since"]
df_diff["No post since"] = df_diff["No post since"].astype(int)
df_diff2 = df_diff[df_diff["No post since"] > 2].sort_values("No post since", ascending=False)
df_diff2 = df_diff2[~df_diff2.Name.isin(ids_removed_from_facebook)]

df_diff2["Link"] = "https://web.facebook.com/" + df_diff2.Name
df_diff2 = df_diff2.reset_index().drop("index", axis=1)
df_diff2.index = df_diff2.index + 1

print(tabulate(pd.concat([pd.DataFrame(df_diff2.columns, index = list(df_diff2.columns)).T, 
           df_diff2])))
