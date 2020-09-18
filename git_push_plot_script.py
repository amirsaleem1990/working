import pandas as pd
import matplotlib.pyplot as plt
import pprint
df=pd.read_csv('~/git_counts.csv')
df = df[df.Count > 0].sort_values('Count', ascending=False).reset_index().drop('index', axis=1)
df['%'] = df.Count / round(df.Count.sum()*100)
pprint.pprint(df)
print(f'\n****  Total count: {df.Count.sum()} ****\n')
plot = plt.bar(df.Repo, df.Count)
plt.tick_params(axis='x', labelsize=14)
if len(df) > 9:
	plt.xticks(rotation=45, ha='center', va='center', rotation_mode='anchor')

for value in plot:
	height = value.get_height()
	plt.text(value.get_x() + value.get_width()/2., 1.002*height,'%d' % int(height), ha='center', va='bottom')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show()