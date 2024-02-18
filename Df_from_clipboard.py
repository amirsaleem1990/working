def Df_from_clipboard():
	import clipboard
	import pandas as pd
	from pprint import pprint
	print("\n\nThe DataFrame with variable name copied in your clipboard, please press CTRL+V\n\n")
	c = pd.read_clipboard()
	s = str(c.to_dict())
	s = f"import pandas as pd, numpy as np; from numpy import nan\ndf = pd.DataFrame({s})\ndf"
	clipboard.copy(s)

	print(c.to_string())