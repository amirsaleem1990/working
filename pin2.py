import pickle
with open("pins.pkl", "rb") as file:
	dic = pickle.load(file)

for e, i in enumerate(sorted(list(dic.keys()))):
		print(e, i)

def addd():
	web_name = input("\nEnter web address:  ")
	email = input("Enter email address: ")
	try:
		dic[web_name][email]
		a = int(input("\nThis email is regestered on this web, are you need to override existing password?\n1-Yes\t\t2-hmmm, show me the existing password\t\t"))
		if a == 1:
			pass
		elif a == 2:
			print("*"*10, dic[web_name][email], "*"*10)
			a = int(input("\nAre you need to override it?\n1-Yes\t\t2-No\t\t"))
			if a == 2:
				return 
			elif a == 1:
				pass
	except:
		pass
	password = input("Enter password: ")
	dic[web_name] = {email : password}
	
	see_dict = int(input("\nAre you want to see added dict?\n1-No\t2-Yes: \t\t"))
	if see_dict == 2:
		import pprint
		print("\n")
		pprint.pprint(dic)
	
	override = int(input("\nAre you need override pin dict?\n1-No\t2-Yes\t\t"))
	if override == 2:
		file_name = "pins.pkl"
	elif override == 1:
		file_name = input("\nEnter New file name: ")
	
	if not file_name.endswith(".pkl"):
		file_name += ".pkl"

	with open(file_name, "wb") as file:
		pickle.dump(dic, file)

def extract():
	a = dict()
	web = int(input("\n\nEnter web name. eg: github\n"))
	print("****** Possible Emails ******")
	print(sorted(list(dic.keys()))[web])
	for e,i in enumerate(dic[sorted(list(dic.keys()))[web]]):
		print(str(e+1) + "- \t" +  i)
		a[str(e+1)] = i
	email = input("\nchoose from numbers\n")
	result = dic[sorted(list(dic.keys()))[web]][a[email]]
	if result:
		print("\n\n*********** Your password is ***********\n" + result)

def add_or_extract():
	print("\n\nYou want add account to data, or Extract data? \n")
	inp = int(input("1-ADD\t2-Extract: \t\t"))
	if inp == 2:
		extract()
	elif inp == 1:
		addd()

add_or_extract()