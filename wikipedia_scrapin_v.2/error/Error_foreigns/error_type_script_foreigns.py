with open('exist_but_not_scraped_foreigns.txt', 'r') as file:
	f = file.readlines()
import sys

f = sorted(list(set([i.strip() for i in f])))
f = [i for i in f if len(i.split()) != 1]

for i in f:
    c = f.index(i)
    if i.startswith('dr. '):
        f[c] = i[4:]
    elif i.startswith('mr. '):
        f[c] = i[4:]
    elif i.startswith('mr '):
        f[c] = i[3:]

names = f

error_dict = {}
ok = []

count = 0
total = len(names)
for i in names:
    count += 1
    print('Ho gay: |{}|\t Baqi hen: |{}|\t{} %'.format(count, total - count, round((count/total), 2)))
    try:
        wikipedia.page(i)
        ok.append(i)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        if exc_type in error_dict:
            error_dict[exc_type].append(i)
        else:
            error_dict[exc_type] = [i]