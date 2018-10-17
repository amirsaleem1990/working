# 1
import wikipedia
import os 
import requests
from bs4 import BeautifulSoup
import pandas as pd


# def wiki_data(name):
#     wiki = wikipedia.page(name)
#     return wiki
# data = wiki_data("nawaz shareef")


# open wikipedia link for this particular person
# os.system('firefox --new-window {}'.format(data.url))
def wiki_persnol_informations(name):
    data = wikipedia.page(name)
    url = data.url
    r  = requests.get(url)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
    info = soup.find("table", { "class" : "infobox vcard" }).select('tr')
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
    new = [i[3:] for i in a if len(i) > 3]
    new = [i for i in new if i.lower() != 'signature']
#     [i for i in new if i[:10] == 'background']

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

    # dict
    # d = dict(zip([final[i] for i in range(0, len(final), 2)],[final[i] for i in range(1, len(final), 2)]))

    df = pd.DataFrame()
    # df[data.original_title] = 
    df['key'] = [final[i] for i in range(0, len(final), 2)]
    df['value'] = [final[i] for i in range(1, len(final), 2)]
    df.to_csv('{}.csv'.format(''.join(data.original_title.split())))
#     os.system('libreoffice {}.csv'.format(''.join(data.original_title.split())))
# for i in ['shahid afridi', 'nawaz shareef', 'barack obama', 'imran khan']:
try:
    os.system("rm -rf /home/amir/Desktop/github/working/new")
except:
    pass

os.mkdir('new')
os.chdir('new/')
# <##    new = [i for i in new if i.lower() != 'signature']>
# 'barack obama','nawaz sharif','shahid afridi''Pervez Musharraf'

#  <new = [i for i in new if i.lower() != 'signature']>
for qq in [ 'imran khan','Michael Jackson','Mian Saqib Nisar', 'Asif Ali Zardari']: 
    try:
        wiki_persnol_informations(qq)
    except:
        print(qq)
