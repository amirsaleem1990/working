import pandas as pd
import time
import os
while True:
	time.sleep(1)
	os.system("du -ch *.pkl | grep total")
	pkls = [i for i in os.listdir() if i.endswith(".pkl")]
	pkls = [i[i.rfind("_")+1:].strip(".pkl") for i in pkls]
	pkls = pd.Series(pkls)
	print(pkls.value_counts())