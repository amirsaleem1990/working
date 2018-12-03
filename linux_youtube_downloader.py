import os
try:
    from pytube import YouTube
except:
    os.system('pip install pytube')
try:
    os.system('subl')
    a = 'subl'
except:
    os.system('gedit')
    a = 'gedit'
if a:
    link = input('Enter your Youtube link: ')
    if link:
    #YouTube(link).streams.first().download()
        quality = int(input([i for i in ['360', '480', '720', '1080']]))
        YouTube(link).streams.filter(subtype='mp4', res="{}p".format(quality)).all()[0].download()
    else:
        with open('youtube_links.txt', 'a+') as file:
            links = file.readlines()
            if links:
                quality = int(input([i for i in ['360', '480', '720', '1080']]))
                print('total videos for download: ', len(links))
                for num, link in enumerate(links):
                    YouTube(link).streams.filter(subtype='mp4', res="{}p".format(quality)).all()[0].download()
                    print(num, '-- completed: ', link)
                print('Download completed....!')
            else:
                print('sorry, you dont give any link..')
                file.write('please Enter some youtube links here')
                file.close()
                os.system('{} youtube_links.txt'.format(a))
else:
    print('install either sublime {} or text {}'.format('https://www.sublimetext.com/3', 'https://help.ubuntu.com/community/gedit'))
os.system('nautilus ./')