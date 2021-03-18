#!/usr/bin/python3
import json
import sys
import os
try:
	file_name = sys.argv[1]
except:
	jupyter_notebooks = [i for i in os.listdir() if i.lower().endswith(".ipynb")]
	if not jupyter_notebooks:
		print("\nSorry, There is no any .ipynb file.")
		sys.exit(1)
	else:
		print("\njupyter files in current directory:")
		for i in list(enumerate(jupyter_notebooks, start=1)):
			print("\t", *i)
		file_name = input("\nPlease give an .ipynb file name, eg: Untitled.ipynb:\n")

x = dict(
	json.load(open(file_name))
	)
xx = '\n'.join([''.join(i['source']) for i in x['cells']])
new_file_name = file_name.strip(".ipynb")+".py"
if os.path.exists(new_file_name):
	new_file_name = input(f"The file <{new_file_name}> exist in current directory, please Enter another name to save it: ")
open(new_file_name, 'w').write(xx)
print(f"\n\nYou file saved as {new_file_name} in current directory.\n")
