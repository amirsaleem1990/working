import pandas as pd
df = pd.read_csv("/home/amir/github/working/Namaz-times/Namaz_2.csv", dtype={"Month" : "object", "Date" : "object"})
df.Month = df.Month.str.lstrip("0").astype(int)
df.Date = df.Date.str.lstrip("0").astype(int)
for i in df.columns.drop(['Month', 'Date']):
    df[i] = df[i].str.lstrip("0").str.replace(":0", ":")
def to_number(x):
    m = x.split(":")
    return int(m[0]) * 60 + int(m[1])
for i in df.columns.drop(['Month', 'Date']):
    df[i] = df[i].apply(to_number)
df["Day"] = (df.Month -1) * 30 + df.Date
def month_str(x):
    dic = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 
           6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 
           11:'Nov', 12:'Dec'}
    return dic[x]
df.Month = df.Month.apply(month_str)
df.Date = df.Date.astype(str) + "-" + df.Month
df = df.sort_values("Day")
df.index = df.Date
df.drop(["Month", "Date", "Day", "Asr_1", "Subah_sadiq"], axis=1, inplace=True)
df = df.rename(columns={"Tulu_aaftab" : "Fajar", "Asr_2": "Asar", "Zawal" : "Zuhar"})
import matplotlib.pyplot as plt
for i in df.columns:
    ax = df[i].plot(figsize=(17,8))
#     h = df[i] // 60
#     m = df[i] & 60
#     yticks_ = h.astype("str") + ":" + m.astype("str")
#     yticks_ = list(yticks_)[::61][::-1]
    ax.set_yticklabels(round(df[i]/60, 2))
    plt.title(i)
    plt.show()