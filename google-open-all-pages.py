import requests
import os
from bs4 import BeautifulSoup
import sys
# url = input("paste your URL: ")
url = sys.argv[1]
soup = BeautifulSoup(requests.get(url).text, "lxml")
for i in soup.select("a"):
    try:
        l = i['href']
        if l.startswith("/url?q="):
            m = l.strip("/url?q=")
            os.system("firefox " + m)
    except:
        pass
