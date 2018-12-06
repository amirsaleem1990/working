import wikipedia
with open('fail_to_extract_data_from_wikipedia(foreigns).txt', 'r') as file:
    foreign = file.readlines()
not_in_wikipedia_foreign = []
 
for i in foreign:
    try:
        wikipedia.page(i)
    except:
        not_in_wikipedia_foreign.append(i)
    print('Ho gay', round((foreign.index(i)/len(foreign))*100, 2))
    
not_in_wikipedia_foreign = [i.lower().strip() for i in not_in_wikipedia_foreign if i and  i != ' ' and i != '\n']
with open('not_in_wikipedia[foreigns].txt', 'w') as file:
    file.write('\n'.join([str(i) for i in not_in_wikipedia_foreign]))
    
with open('fail_to_extract_data_from_wikipedia(from_pakistan).txt', 'r') as file:
    pakistan = file.readlines()
not_in_wikipedia_pakistan = []
 
for i in pakistan:
    try:
        wikipedia.page(i)
    except:
        not_in_wikipedia_pakistan.append(i)
    print('Ho gay', round((pakistan.index(i)/len(pakistan))*100, 2))
not_in_wikipedia_pakistan = [i.lower().strip() for i in not_in_wikipedia_pakistan if i and  i != ' ' and i != '\n']
with open('not_in_wikipedia[from_pakistan].txt', 'w') as file:
    file.write('\n'.join([str(i) for i in not_in_wikipedia_pakistan]))