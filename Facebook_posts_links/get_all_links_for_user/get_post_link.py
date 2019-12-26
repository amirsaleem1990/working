with open("/home/amir/AB/15_MMushtaqYusufzai.pkl", "rb")  as file:
    soup = BeautifulSoup(pickle.load(file))
    
LINKS = []
for i in soup.select("a"):
    try:
        link = i['href']
        if link.startswith("/story.php?story_fbid="):
            link = link.split("=")[1].split("&id=")[0].strip("&id")
            link = "https://web.facebook.com/MMushtaqYusufzai/posts/" + link
            LINKS.append(link)
    except:
        pass
    
for i in set(LINKS):
    os.system("firefox " + i)