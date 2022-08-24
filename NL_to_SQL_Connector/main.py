from connect_to_db import connectToDigitalOcean
import pandas as pd


dataFrame = pd.read_sql("SELECT DISTINCT MAKE FROM DT_test_Table1", con=connectToDigitalOcean())