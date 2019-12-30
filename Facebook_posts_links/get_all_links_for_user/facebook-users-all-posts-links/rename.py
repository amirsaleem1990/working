import os
import pickle
import pandas as pd

os.chdir("Extracted")
folders = os.listdir()

for folder in folders:
    os.chdir(folder)
    local_files = os.listdir()
    for file in local_files:
        if not file.startswith("LINK"):
            number = file.split("_")[0]
            if len(number) == 1:
                ok_name = "000" + file
            elif len(number) == 2:
                ok_name = "00" + file
            elif len(number) == 3:
                ok_name = "0" + file
            else:
                ok_name = file
            os.rename(file, ok_name)
    os.chdir("../")