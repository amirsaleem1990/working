#!/usr/bin/python3
# https://stackoverflow.com/questions/50197643/youtbe-dl-multiple-downloads-at-the-same-time
import multiprocessing.dummy
import subprocess
import os

os.remove("_Errors_.txt")

def download(url):
	try:
		subprocess.check_call([
			'youtube-dl', url])
		open("downloaded.txt", "a").write(url+"\n")
	except:
		print("\n\nERROR --------------------------------------------------")
		print(f"url: {url}")
		e_ = traceback.format_exc()
		print(e_)
		print("---------------------------------------------- Error END\n\n")

		open("_Errors_.txt", 'a').wirte(f'---------------------------------\nUrl:{url}\n{e_}\n\n')

try:
	arr = [i for i in set(open("mp4_links.txt", "r").read().splitlines()) if i.strip()]
except:
	file_name = input("file <mp4_links.txt> not found, please Enter your file name: ")
	arr = [i for i in set(open(file_name, "r").read().splitlines()) if i.strip()]

try:
	downloaded = open("downloaded.txt", "r").read().splitlines()
	arr = [i for i in arr if not i in downloaded]
except:
	pass
	
p = multiprocessing.dummy.Pool()
p.map(download, arr)
