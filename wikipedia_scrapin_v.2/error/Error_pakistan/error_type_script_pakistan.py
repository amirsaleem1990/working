import sys
import wikipedia

p = open('exist_but_not_scraped_pakistan_2.txt', 'r')
p = p.readlines()
p = sorted([i.strip() for i in p])


for i in p:
    c = p.index(i)
    if i.startswith('dr. '):
        p[c] = i[4:]
    elif i.startswith('air vice marshal'):
        p[c] = i[16:]
    elif i.startswith('ch. '):
        p[c] = i[4:]
    elif i.startswith('dr. '):
        p[c] = i[4:]
    elif i.startswith('lt gen '):
        p[c] = i[7:]
    elif i.startswith('maj gen '):
        p[c] = i[8:]
    elif i.startswith('mr, '):
        p[c] = i[4:]
    elif i.startswith('mr. '):
        p[c] = i[4:]
    elif i.startswith('ms. '):
        p[c] = i[4:]
with open('exist_but_not_scraped_pakistan_3.txt', 'w') as file:
    file.write('\n'.join(p))

names = p


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