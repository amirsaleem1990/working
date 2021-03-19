#!/usr/bin/python3
# https://stackoverflow.com/questions/50197643/youtbe-dl-multiple-downloads-at-the-same-time
import multiprocessing.dummy
import subprocess


arr = [{'url' : i} for i in set(open("mp4_links.txt", "r").read().splitlines()) if i.strip()]
try:
	downloaded = open("downloaded.txt", "r").read().splitlines()
	arr = [i for i in arr if not i['url'] in  downloaded]
except:
	pass
	
def download(v):
	try:
		subprocess.check_call([
			'youtube-dl', v['url']])
		open("downloaded.txt", "a").write(v['url']+"\n")
	except:
		pass
p = multiprocessing.dummy.Pool()
p.map(download, arr)
 