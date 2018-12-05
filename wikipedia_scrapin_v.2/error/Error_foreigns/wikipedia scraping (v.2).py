import wikipedia
import os 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys

def wiki_persnol_informations(name):

    data = wikipedia.page(name)
    url = data.url
    r  = requests.get(url)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
    try:
        info = soup.find("table", { "class" : "infobox vcard" }).select('tr')
    except:
        info = soup.find("table", { "class" : "infobox biography vcard" }).select('tr')
    d = {}
    for i in range(len(info)):
        try: 
            if 'background' in str(info[i].select_one('th')):
                a = info[i].select_one('th').text
                d[a.lower().replace(',', '|')] = 'th  background'
            else:    
                a = info[i].select_one('th').text
                d[a.lower().replace(',', '|')] = 'th'
            a = ''
        except:
            pass
        try:
            b = info[i].select_one('td').text
            d[b.lower().replace(',', '|')] = 'td'
            b = ''
        except: pass
    try:
        d.pop('\n')
        d.pip(' ')
    except:
        pass

    df = pd.DataFrame()
    key = []
    value = []
    for k,v in d.items():
        if not k.startswith('signat'):
            key.append(k)
            value.append(v)
    key = [i.replace(',', '|') for i in key]
    df['key'] = key
    df['value'] = value

    start = df[df['key'].str.startswith('personal')]
    start_1 = start.index[0]+1
    if len(start.index) > 1:
        last_1 = start.index[-1]+1
    else:
        last_1 = len(df)
    last_2 = df.iloc[last_1:]
    if len(start.index) > 1:
        last = last_2[last_2['value'] == 'th  background'].index[0]
    persnol_info = df.iloc[start_1: last_1]
    if len(start.index) > 1:
        persnol_info.drop(persnol_info[persnol_info['value'].str.endswith('background')].index[0], inplace=True)

    
    final_1 = pd.DataFrame()
    p = persnol_info
    th = list(p[p['value'] == 'th']['key'])
    td = list(p[p['value'] == 'td']['key'])
    final_1['th'] = th
    final_1['td'] = td
    final_1 = final_1.T
    final_1.to_csv('{}.csv'.format(''.join(data.original_title.split())), index = False, header = False)
#     local_dict = final_1.to_dict()
#     print(len(global_dict))
#     for key,value in local_dict.items():
#         if key in global_dict:
#             global_dict[key].append(value)
#         else:
#             global_dict[key] = [np.nan]*len(global_dict) + [value]
    
    
    
    
fail_list = []

with open('exist_and_no_error_but_notscraped_yed.txt', 'r') as file:
	names = file.read()
names = names.split('|')

ok_names = []
error_dict = {}
count = 0
total = len(names)
for i in names:
	count += 1
	try:
		wiki_persnol_informations(i)
		ok_names.append(i)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		if exc_type in error_dict:
		    error_dict[exc_type].append(i)
		else:
		    error_dict[exc_type] = [i]
	print('Ho gay: |{}|\t Baqi hen: |{}|\t {}'.format(count, total - count, round((count / total)*100, 2)), '\t', len(ok_names))

with open('exist_and_no_error_but_notscraped_yet_2.txt', 'w') as file:
	file.write('\n'.join([i for i in names if i not in ok_names]))

import pickle
with open('error_type_script_pakistan_2.py', 'wb') as file:
	pickle.dump(error_dict, file)
