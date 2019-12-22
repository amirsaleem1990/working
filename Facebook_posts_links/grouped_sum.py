import pandas as pd
import time
import os
while True:
	time.sleep(1)
	print("*****************************************************************")
	os.system("date +%H:%M:%S")
	os.system("echo -e $(du -c -BM *.pkl | grep total | cut -d 'M' -f 1) \t\t\t MB")
	pkls = [i for i in os.listdir() if i.endswith(".pkl")]
	pkls = [i[i.rfind("_")+1:].strip(".pkl") for i in pkls]
	pkls = pd.Series(pkls)
	print(pkls.value_counts())