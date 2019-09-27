import os
lst = []
while True:
	i = input("Enter PID <number> [or <q> for quit]:  ")
	if i == "q":
		break
	else:
		try:
			lst.append(int(i))
		except:
			print("Enter a PID <in number> or press <q> for quit")
			pass

lst = [29001, 24777, 10296, 24326]
s = 0
for i in lst:
	a = list(os.popen("sudo pmap {} | grep total".format(i)))
	s += int(''.join([ii for ii in a[0] if ii.isnumeric()]))
# if s < 1024:
# 	print(f"{s} KB")
# elif s < 1024*1024:
# 	print(f"{s/1024} MB")
# elif s < 1024*1024*1024:
# 	print(f"{s/1024/1024} GB")
print("KB: ", s)
print("MB: ", round(s/1024, 2))
print("GB: ", round(s/1024/1024, 4))