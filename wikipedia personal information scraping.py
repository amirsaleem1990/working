import wikipedia
import os 
import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    ls = []
    for i in range(len(info)):
        try: 
            if 'background' in str(info[i].select_one('th')):
                a = info[i].select_one('th').text
                ls.append('th ' + 'background ' + a)
            else:    
                a = info[i].select_one('th').text
                ls.append('th ' + a)
            a = ''
        except:
            pass
        try:
            b = info[i].select_one('td').text
            ls.append('td ' + b)
            b = ''
        except: pass
    a = [i.replace('\n', '') for i in ls if i != '\n']
    #     [i for i in a if i[:2] == 'th']
    new = [i[3:] for i in a if len(i) > 4]
    new = [i for i in new if i.lower() != 'signature']
    #     [i for i in new if i[:10] == 'background']
    if 'signature' in ' '.join(new):
        c = -1
        m = 0
        q = ''
        for i in new:
            c += 1
            if i[:19] == 'background Personal':
                start = new[c:]
                q = 'ok'
                break
        if q == 'ok':
            m = c
            for i in new[c+1:]:
                m += 1
                if i[:10] == 'background':
                    pass
                    break
        final = new[c+1:m]
    else:
        final = new
    d = dict(zip([final[i] for i in range(0, len(final), 2)],[final[i] for i in range(1, len(final), 2)]))
    df = pd.DataFrame()
    df['key'] = d.keys()
    df['value'] = d.values()
    df.to_csv('{}.csv'.format(''.join(data.original_title.split())))
#     os.system('libreoffice {}.csv'.format(''.join(data.original_title.split())))
try:
    os.system("rm -rf /new")
except:
    pass

os.mkdir('new')
os.chdir('new/')

for i in['imran khan','barack obama','nawaz sharif','shahid afridi','Pervez Musharraf','Michael Jackson','Mian Saqib Nisar', 'Asif Ali Zardari']:
    try:
            a = wiki_persnol_informations(i)
    except:
        print(i)