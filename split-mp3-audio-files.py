s = [24,  "Ae-allah.mp3",
19,  "Ae-rasool-e-ameen.mp3",
23,  "Ae-taiba.mp3",
46,  "Badr-u-dduja.mp3",
17,  "Banun-ga-me-hafiz-e-quran.mp3",
21,  "Ilahi-teri-chokehat-pe.mp3",
11,  "Jaga-g-lagany-ki.mp3",
13,  "Jalwa-e-Janan.mp3",
16,  "Mai-bhi-madarse-jaunga.mkv.mp3",
# 8,  "Mai-bhi-roze-rakhunga.opus",
15,  "Meetha-meetha-pyaara.mp3",
17,  "Me-ne-tmhe-dekha-hai.webm.mp3",
10,  "Meri-maa-pyari-maa.mp3",
46,  "Mohammad-ka-roza.mp3"]

# files names
names = s[1::2]

# from second we want tha audio
fromm = [s[0]] + s[2::2]

import os
for f, name in zip(fromm, names):
        # full time of audio in seconds
        full_time = int(list(os.popen('mp3info -p "%S" ' + name))[0])
        
        # minutes in audio
        mins = int(full_time/60)
        
        # seconds in audio
        seconds = full_time - (mins*60)
        
        # for give audio extract from <f> to 00:mins:seconds and save it by same orignal name by adding <ok.mp3> in the end
        command = f"ffmpeg -i {name} -vn -acodec copy -ss 00:00:{f} -to 00:{mins}:{seconds} {name}_ok.mp3" 
        os.system(command)