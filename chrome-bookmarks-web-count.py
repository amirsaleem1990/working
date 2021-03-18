#!/usr/bin/python3

import json
import pandas as pd

x = json.load(open('/home/amir/.config/google-chrome/Default/Bookmarks', 'r'))
x = x['roots']['bookmark_bar']['children']
df = pd.DataFrame.from_dict(x)
df = df.drop(columns=['type', 'id', 'meta_info'])
print(df.url.str.strip('https://www.|http://www.').str.split("/").str[0].value_counts().to_string())