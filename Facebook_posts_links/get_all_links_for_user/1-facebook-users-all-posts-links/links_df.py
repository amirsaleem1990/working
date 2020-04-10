import os
import pandas as pd
import pickle
from bs4 import BeautifulSoup
orignal_dir = os.getcwd()
os.chdir("/home/amir/Extracted")
folders = os.listdir()
LINKS = []
for fb in folders:
    os.chdir(fb)
    files = os.listdir()
    files = [i for i in files if i.endswith(".pkl") and not i.startswith("LINK")]
    for f in files:
        with open(f, "rb")  as file:
            soup = BeautifulSoup(pickle.load(file))
        for i in soup.select("a"):
            try:
                link = i['href']
                if link.startswith("/story.php?story_fbid="):
                    link = link.split("=")[1].split("&id=")[0].strip("&id")
                    link = f"https://web.facebook.com/{fb}/posts/" + link
                    if not link in LINKS:
                        LINKS.append([fb, link])
            except:
                pass
    os.chdir("../")
os.chdir(orignal_dir)

df = pd.DataFrame(LINKS)
df = df.drop_duplicates()
df.columns = ["Name", "Link"]

df.to_csv("Links.csv", index=False)
gopen("Links.csv")