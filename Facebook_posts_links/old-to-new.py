import pickle
with open("All_FB_links.pkl", "rb") as file:
    d = pickle.load(file)
dd = {}
import pandas as pd
for i in d:
    dd[i] = [(v, "before 20-sep-2019") for v in d[i]]
df = pd.DataFrame()
for i in dd:
    adf =  pd.DataFrame(dd[i])
    adf['Name'] = i
    df = df.append(adf)
df.to_csv("links.csv", index=False)
