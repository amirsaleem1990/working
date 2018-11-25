import os
from pydub import AudioSegment
os.chdir('The_English_We_Speak/')
all_folders = os.listdir()
for folder in all_folders:
    os.chdir(folder)
    folder_items = !ls
    audio_file = [i for i in folder_items if 'mp3' in i]
    if audio_file:
        audio_file = audio_file[0]
        sound = AudioSegment.from_mp3(audio_file)
        except_first_13_seconds = sound[13000:]
        os.remove(audio_file)
        except_first_13_seconds.export(audio_file, format="mp3")
    else:
        pass
    os.chdir('..')