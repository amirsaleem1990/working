df = pd.read_csv("Namaz.csv")
def to_24_hours(x):
    return x + 12
columns_to_24_hours = ['Asr 1', 'Asr 2', 'Magrib', 'Isha']
df[columns_to_24_hours] = df[columns_to_24_hours].apply(to_24_hours)
# df.head()

for i in df.columns:
    df[i] = df[i].astype(str)
def add_zero(x):
    if x.name == "Month":
        return x
    return pd.Series([i if len(i) == 2 else "0" + i for i in x])
df = df.apply(add_zero)
# df.head()

Subah_sadiq = df.iloc[:, 0] + ":" + df.iloc[:, 1]
Tulu_Aftab  = df.iloc[:, 2] + ":" + df.iloc[:, 3]
Zawal       = df.iloc[:, 4] + ":" + df.iloc[:, 5]
Asr_1       = df.iloc[:, 6] + ":" + df.iloc[:, 7]
Asr_2       = df.iloc[:, 8] + ":" + df.iloc[:, 9]
Magrib      = df.iloc[:, 10] + ":" + df.iloc[:, 11]
Ish         = df.iloc[:, 12] + ":" + df.iloc[:, 13]
df = df.drop(df.columns[:14], axis=1)
df = pd.concat([df, pd.DataFrame([Subah_sadiq, Tulu_Aftab, Zawal, Asr_1, Asr_2, Magrib, Ish]).T], axis=1)
df.columns = ["Month", "Date", "Subah_sadiq", "Tulu_aaftab", "Zawal", "Asr_1", "Asr_2", "Magrib", "Isha"]
df.Month = df.Month.map({"Feb" : "02", "March" : "03", "April" : "04", "June" : "06","May" : "05","Nov" : "11",
                         "Jan" : "01","Sep" : "09","Dec" : "12","Oct" : "10","Jul" : "07","Aug" : "08"})
# df.head()
df.to_csv("Namaz_2.csv", index=False)