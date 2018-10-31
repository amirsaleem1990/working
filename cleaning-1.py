import pandas as pd
import numpy as np
df = pd.read_excel('SaqibA.xlsx')
df['Description of Goods and/or Services'] = [str(i).lower() for i in df['Description of Goods and/or Services']]
df = df[['Description of Goods and/or Services']]
ls2 =  [str(i).replace('kgs', ' KGS ')
         .replace("'", '')
         .replace("''", '')
         .replace('quantity', ' QTY ')
         .replace('quanity', ' QTY ')
         .replace('qty', ' QTY ')
         .replace('lbs', ' LBS ')
         .replace('meter', " METER ")
         .replace('bags' , ' BAGS ')
         .replace('units' , " UNITS ")
         .replace('mts', ' MTS ')
         .replace('mt ', ' MT ')
         .replace('mtr ', ' METER ')
         .replace('mtrs', ' METER ')
         .replace('m.ton', ' MTS ')
         .replace('tons', ' TONS ')
         .replace('sqft', ' SQFT ')
         .replace('sq.ft', ' SQFT ')
         .replace('sqmt', ' SQMT ')
         .replace('yds', ' YDS ')
         .replace('yards', ' YDS ')
         .replace('yds', ' YDS ')
         .replace(':', '')
         .replace('yrd', ' YDS ')
         .replace('yard', ' YDS ')
         .replace('\n', '')
         .replace('\r', ' ')
         .replace('-', '')
         .replace(',', '')
         .replace('..', '')
         .replace('  ', ' ')
         .replace('   ', ' ')
         .replace('    ', ' ')
         .replace('     ', ' ')
         .replace('      ', ' ')
         .replace('+', '')
         .replace('pcs', ' PCS ')
         .replace('unit', ' UNITS ')
         .replace('mtrs ', 'METERS ') for i in df['Description of Goods and/or Services']]
df['ls2'] = ls2

multiple = []
none = []
c = -1
for i in df['ls2']:
    c += 1
    a = str(i)
    b = list(str(i))
    su = sum([z.isnumeric() for z in b])
    if su < 3:
        if ('PCS' not in a) and ('UNITS' not  in a)  and ('QTY' not in a) and ('KGS' not in a)  and ('LBS'  not in a)  and ('METER' not in a)  and ('BAGS' not in a)  and ('MTS' not in a)  and ('MT' not in a )  and ('TONS' not in a)  and ('SQFT' not in a)   and ('SQMT' not in a)  and  ('YDS'  not in a)  and ('METERS' not in a):
            none.append(c)
    m = a.split()
    if ('lot 2' in a) or ((m.count('QTY') > 1 and m.count('KGS') > 1)) or (a[:2] == '1.' and ' 2. ' in a) or (a[:2] == '1)' and ' 2)' in a):
        multiple.append(c)

accur = []
for i in range(len(df)):
    if i in multiple:
        accur.append('multiple')
    elif i in none:
        accur.append('NONE')
    else:
        accur.append('not sure')
df['accur'] = accur

v = ['PCS', 'UNITS', 'KGS', 'LBS', 'METER', 'BAGS', 'MTS', 'MT', 'TONS', 'SQFT', 'YDS', 'METERS']
filtr = []
ind_filter = []
for i in df.ls2:
    a = str(i)
    m = a.split()
    if 'PCS' in a:
        filtr.append('PCS')
        ind_filter.append(m[m.index('PCS')-1])
                          
    elif 'UNITS' in a:
        filtr.append('UNITS')
        ind_filter.append(m[m.index('UNITS')-1])
        
    elif 'KGS' in a:
        filtr.append('KGS')
        ind_filter.append(m[m.index('KGS')-1])
                          
    elif 'LBS' in a:
        filtr.append('LBS')
        ind_filter.append(m[m.index('LBS')-1])
    
    elif 'METER' in a:
        filtr.append('METER')
        ind_filter.append(m[m.index('METER')-1])
    
    elif 'BAGS' in a:
        filtr.append('BAGS')
        ind_filter.append(m[m.index('BAGS')-1])
        
    elif 'MTS' in a:
        filtr.append('MTS')
        ind_filter.append(m[m.index('MTS')-1])
        
    elif 'MT' in a:
        filtr.append('MT')
        ind_filter.append(m[m.index('MT')-1])
        
    elif 'TONS' in a:
        filtr.append("TONS")
        ind_filter.append(m[m.index('TONS')-1])
        
    elif 'SQFT'  in a:
        filtr.append('SQFT')
        ind_filter.append(m[m.index('SQFT')-1])
        
    elif 'YDS' in a:
        filtr.append('YDS')
        ind_filter.append(m[m.index('YDS')-1])
        
    elif 'METERS' in a:
        filtr.append("METERS")
        ind_filter.append(m[m.index('METERS')-1])
        
    else:
        filtr.append('not sure')
        ind_filter.append('not sure')
df['filterr'] = filtr

z = []
for i in range(len(df)):
    st = df[i:i+1]['ls2'].values[0]
    fltr = df[i:i+1]['filter'].values[0]
    ind = st.find(fltr)
    if ind < 10:
             z.append(st[:15])
    else:
             z.append(st[ind-10: ind+10])
            
df['important'] = z
df['ind_filter'] = ind_filter
df.to_csv('new.csv')
# os.system('libreoffice new.csv')