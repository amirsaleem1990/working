import time
import os
import datetime
a = os.popen("ls *.mp3 | wc")
b = int(list(a)[0].split()[0])

while True:
	time.sleep(5)
	c = os.popen("ls *.mp3 | wc")
	d = int(list(c)[0].split()[0])
	if d > b:
	    m = os.popen("du -sh")
	    t = datetime.datetime.now()
	    print(d, "\t\t\t", list(m)[0].split('\t')[0], str(t.hour) + ":" + str(t.minute) + ":" + str(t.second))
	    b = d