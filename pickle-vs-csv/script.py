#!/home/amir/pickle-vs-csv/Virtual-env/bin/python3
import pandas as pd
import pickle
import pickle5 as pickle_
import shutil
import os
import time
import warnings
warnings.filterwarnings('ignore')
import sqlalchemy

class Speed_comparison_for_load_and_dump:

	def __init__(self):
		self.csv_files = [i for i in os.listdir() if i.endswith(".csv")]
		self.pickle_files = [i for i in os.listdir() if i.endswith(".pkl")]

		self.df = None
		self.summary_lst = []
		self.total_files = sum([(i.endswith(".pkl") or i.endswith(".pkl")) for i in os.listdir()])
		self.completed_files = 0


	def connect_to_db(self):
		print("connect_to_db method called")
		user = 'amir_saleem'
		passw = 'passw0rd'
		host =  '127.0.0.1'
		port = 3306
		database = 'amir_experiment' 
		conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}/{database}')
		self.conn = conn.connect()

	def load_data(self, file_name, extention):

		# print("load_data method is called")

		if not file_name in os.listdir():
			return

		if extention == "pkl":
			try:
				start_time = time.time()
				self.df = pd.read_pickle(file_name)
			except:
				try:
					start_time = time.time()
					self.df = pickle.load(open(file_name, 'rb'))
				except:
					try:
						start_time = time.time()
						self.df = pickle_.load(open(file_name, 'rb'))
					except:
						return
		elif extention == "csv":
			try:
				start_time = time.time()
				self.df = pd.read_csv(file_name)
			except:
				return
		else:
			return 

		end_time = time.time()
		self.sumamry(
			file_name = file_name, 
			row = self.df.shape[0], 
			cols = self.df.shape[1], 
			size = self.df.memory_usage(deep=True).sum(), 
			time = end_time - start_time,
			extention = extention,
			action = "load"
			)
	def save_in_db(self, table_name):
		try:
			# print("save_in_db method is called")
			if table_name in [i[0] for i in list(self.conn.execute("show tables;"))]:
				return
			start_time = time.time()
			self.df.to_sql(table_name, con=self.conn)
			end_time = time.time()

			self.sumamry(
				file_name = table_name, 
				row = self.df.shape[0], 
				cols = self.df.shape[1], 
				size = self.df.memory_usage(deep=True).sum(), 
				time = end_time - start_time,
				extention = "db",
				action = "dump"
				)

		except Exception as e:
			open("Errors.txt", 'a').write(table_name + "\n" + str(e)+"\n------------------\n\n")
			pass

	def save_in_csv(self, file_name):
		try:
			# print("save_in_csv method is called")
			start_time = time.time()
			# if file_name in os.listdir():
			# 	return
			self.df.to_csv(file_name, index=False)
			end_time = time.time()

			self.sumamry(
				file_name = file_name, 
				row = self.df.shape[0], 
				cols = self.df.shape[1], 
				size = self.df.memory_usage(deep=True).sum(), 
				time = end_time - start_time,
				extention = "csv",
				action = "dump"
				)

		except Exception as e:
			open("Errors.txt", 'a').write(file_name + "\n" + e+"\n------------------\n\n")

	def save_in_pkl(self, file_name):
		try:
			# print("save_in_pkl method is called")
			# if file_name in os.listdir():
			# 	return
			start_time = time.time()
			self.df.to_pickle(file_name)
			end_time = time.time()
			self.sumamry(
				file_name = file_name, 
				row = self.df.shape[0], 
				cols = self.df.shape[1], 
				size = self.df.memory_usage(deep=True).sum(), 
				time = end_time - start_time,
				extention = "pkl",
				action = "dump"
				)


		except Exception as e:
			open("Errors.txt", 'a').write(file_name + "\n" + e+"\n------------------\n\n")

	def read_from_table(self, table_name):

		if not table_name in [i[0] for i in list(self.conn.execute("show tables;"))]:
			return
		try:
			# print("read_from_table method is called")
			start_time = time.time()
			self.df = pd.read_sql_table(table_name, con=self.conn)
			end_time = time.time()
			self.sumamry(
				file_name = table_name, 
				row = self.df.shape[0], 
				cols = self.df.shape[1], 
				size = self.df.memory_usage(deep=True).sum(), 
				time = end_time - start_time,
				extention = "db",
				action = "load"
				)
		except Exception as e:
			open("Errors.txt", 'a').write(table_name + "\n" + e+"\n------------------\n\n")

	def remove_a_file(self, file_name):
		# print("remove_a_file method is called")
		os.remove(file_name)

	def remove_table(self, table_name):
		# print("remove_table method is called")
		if not table_name in [i[0] for i in list(self.conn.execute("show tables;"))]:
			return
		command = f"DROP TABLE `{table_name}`;"
		self.conn.execute(command)


	def prepare_data_method(self):
		# print("prepare_data_method method is called")
		if (not self.csv_files) and (not self.pickle_files):
			raise Exception("\nNo pickle or csv file found\n")

		for csv_file in self.csv_files:
			# print("\n>>>>>>>>> File:", csv_file)
			self.load_data(file_name=csv_file, extention="csv")
			self.save_in_pkl(csv_file.replace(".csv", ".pkl"))
			self.save_in_db(table_name=csv_file.replace(".csv", ""))

		for pickle_file in self.pickle_files:
			self.load_data(file_name=pickle_file, extention="pkl")
			self.save_in_csv(pickle_file.replace(".pkl", ".csv"))
			self.save_in_db(table_name=pickle_file.replace(".pkl", ""))


	def remove_files_that_dont_have_pair(self):
		# print("remove_files_that_dont_have_pair method is called")
		current_files = os.listdir()
		base_names = [i.replace(".pkl", "").replace(".csv", "") for i in current_files if (i.endswith(".pkl")) or (i.endswith(".csv")) ]
		base_names = [i for i in set(base_names) if base_names.count(i)  != 2]
		lst = []
		for i in base_names:
			if i+".csv" in current_files:
				lst.append(i+".csv")
			elif i+".pkl" in current_files:
				lst.append(i+".pkl")
		current_files = lst
		self.csv_files = [i for i in os.listdir() if i.endswith(".csv")]
		self.pickle_files = [i for i in os.listdir() if i.endswith(".pkl")]
		if len(self.csv_files) != len(self.pickle_files):
			raise Exception("Some files don't have pair.")

	def sumamry(self, file_name, row, cols, size, time, extention, action):
		# print("sumamry method is called")
		self.summary_lst.append(
			[file_name, row, cols, size, time, extention, action]
			)
		pickle.dump(self.summary_lst, open("summary.pkl", 'wb'))
		if self.completed_files % 20 == 0:
			print(f"total_files:{self.total_files}, completed_files:{self.completed_files})")


	def create_a_summary(self):
		# print("create_a_summary method is called")
		current_files = [i for i in os.listdir() if i in self.pickle_files + self.csv_files]
		self.current_files = len(current_files)
		base_names = [i.replace(".pkl", "").replace(".csv", "") for i in current_files ]
		for file in base_names:
			self.load_data(file_name=file+".csv", extention="csv")
			self.load_data(file_name=file+".pkl", extention="pkl")
			self.read_from_table(file)

			# self.remove_a_file(file + ".pkl")
			# self.remove_a_file(file + ".csv")
			# self.remove_table( file )

	def loop(self):
		print("loop method is called")
		if (not self.csv_files) and (not self.pickle_files):
			raise Exception("\nNo pickle or csv file found\n")

		for csv_file in self.csv_files:
			# print("\n>>>>>>>>> File:", csv_file)

			pickle_name_ = csv_file.replace(".csv", ".pkl")
			table_name_ = csv_file.replace(".csv", "")

			self.load_data(file_name=csv_file, extention="csv")
			self.save_in_csv(csv_file)

			self.save_in_pkl(pickle_name_)
			self.load_data(file_name=pickle_name_, extention="pkl")

			self.save_in_db(table_name=table_name_)
			self.read_from_table(table_name=table_name_)

			self.remove_table(table_name_)
			self.remove_a_file(pickle_name_)

			self.completed_files += 1

		for pickle_file in self.pickle_files:
			# print("\n>>>>>>>>> File:", pickle_file)

			csv_name_ = pickle_file.replace(".pkl", ".csv")
			table_name_ = pickle_file.replace(".pkl", "")

			self.load_data(file_name=pickle_file, extention="pkl")
			self.save_in_pkl(pickle_file)

			self.save_in_csv(csv_name_)
			self.load_data(file_name=csv_name_, extention="csv")

			self.save_in_db(table_name=table_name_)
			self.read_from_table(table_name=table_name_)

			self.remove_table(table_name_)
			self.remove_a_file(csv_name_)

			self.completed_files += 1

	def main(self):
		print("main method is called")
		self.connect_to_db()
		# before = len(setf.pickle_files)
		self.pickle_files = [table_name for table_name in self.pickle_files if not table_name in [i[0] for i in list(self.conn.execute("show tables;"))]]
		self.csv_files = [table_name for table_name in self.csv_files if not table_name in [i[0] for i in list(self.conn.execute("show tables;"))]]
		# self.prepare_data_method()
		# self.remove_files_that_dont_have_pair()
		# self.create_a_summary()
		self.loop()


obj = Speed_comparison_for_load_and_dump()
obj.main()







import os
import pandas as pd
x =[i for i in os.listdir() if i.endswith(".pkl") or i.endswith(".csv")]
df = pd.DataFrame({'actual':x})
df['withoud_extention'] = df.actual.str.replace(".pkl$", "").str.replace(".csv$", "")
to_remove = df[df.duplicated(subset="withoud_extention", keep='first')].actual.to_list()
for file_to_remove in to_remove:
	os.remove(file_to_remove)
import sqlalchemy
user = 'amir_saleem'
passw = 'passw0rd'
host =  '127.0.0.1'
port = 3306
database = 'amir_experiment' 
conn = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@{host}/{database}')
conn = conn.connect()
for i in [i[0] for i in list(conn.execute("show tables;"))]:
	conn.execute(f"drop table `{i}`;")
exit()