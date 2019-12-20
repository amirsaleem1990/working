# see days since last post 
os.system("ipython3 links-pickle-to-df.py")
previos_data = pd.read_csv("All_FB_links_names_corrected.csv")

crnt_time = pd.to_datetime(
	datetime.datetime.now(),
	infer_datetime_format=True)

	last_date = pd.to_datetime(
		previos_data[previos_data.Name == fb].tail(1).Tate.values,
			infer_datetime_format=True)
	last_post_was_before_days = abs(int(str(list((last_date - crnt_time))[0]).split()[0]))
	if not len(last_post_was_before_days):
		last_post_was_before_days = "NA"
	LPM.append((fb, last_post_was_before_days))