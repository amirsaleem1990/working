# go to ~/.ipython/profile_default/startup
# create a file <start.py
>
# add these lines in the file:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from datetime import datetime
import pickle 
import requests
from bs4 import BeautifulSoup
import pandas_profiling

# Pandas options
pd.options.display.max_columns = 30
pd.options.display.max_rows = 20

