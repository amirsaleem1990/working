import pandas as pd
import time
import os
while True:
	time.sleep(10)
	os.system("du -sh *.pkl")
	pkls = [i for i in os.listdir() if i.endswith(".pkl")]
	pkls = [i[i.rfind("_")+1:].strip(".pkl") for i in pkls]
	pkls = pd.Series(pkls)
	pkls.value_counts()