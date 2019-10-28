import pandas as pd
import pickle
with open("All_FB_links_names_corrected.pkl", "rb") as file:
	d = pickle.load(file)
dd = {}
names = []
for i in d:
	lst = d[i]
	c = 0
	for z in lst:
		c += 1
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

	names += [i] * c
ls = [pd.DataFrame(dd[i]) for i in dd]

df = pd.concat(ls).reset_index().drop("index", axis=1)
df['name'] = names
df.to_csv("All_FB_links_names_corrected.csv", index=False)