import pandas as pd
import pickle
with open("/home/amir/github/working/Facebook_posts_links/All_FB_links_names_corrected.pkl", "rb") as file:
	d = pickle.load(file)
dd = {}
names = []
for i in d:
	links = d[i]
	names += [i] * len(links)
	for z in links:
		if isinstance(z, tuple):
			if i in dd:
				dd[i].append(z)
			else:
				dd[i] = [z]
		else:
			if i in dd:
				dd[i].append((z, "TIME not recorded"))
			else:
				dd[i] = [(z, "TIME not recorded")]

ls = [pd.DataFrame(dd[i]) for i in dd]

df = pd.concat(ls).reset_index().drop("index", axis=1)
df['name'] = names
df.columns = ["Link", "Tate", "Name"]
df.to_csv("/home/amir/github/working/Facebook_posts_links/All_FB_links_names_corrected.csv", index=False)