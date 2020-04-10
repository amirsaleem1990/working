import pickle
import pandas as pd
with open("All_FB_links_names_corrected.pkl", "rb") as file:
	d = pickle.load(file)
import datetime
#now = datetime.datetime.now()
#str(now)
dd = {}

for i in d:
    dd[i] = [(v, "before 20-sep-2019") for v in d[i]]
df = pd.DataFrame()
for i in dd:
    adf =  pd.DataFrame(dd[i])
    adf['Name'] = i
    df = df.append(adf)
df.columns = ["link", "Date", "Name"]
df.to_csv("links.csv", index=False)
