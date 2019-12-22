import pandas as pd
import time
import os
while True:
	time.sleep(60)
	print("*****************************************************************")
	os.system("date +%H:%M:%S")
	os.system("echo $(du -c -BM *.pkl | grep total | cut -d 'M' -f 1) MB")
	pkls = [i for i in os.listdir() if i.endswith(".pkl")]
	pkls = [i[i.rfind("_")+1:].strip(".pkl") for i in pkls]
	pkls = [i for i in pkls if i != "corrected"]
	pkls = pd.Series(pkls)
	print(pkls.value_counts())