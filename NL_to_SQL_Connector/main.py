from connect_to_db import connectToDigitalOcean
import pandas as pd


dataFrame = pd.read_sql("SELECT DT_ID FROM  DT_test_Table1  WHERE ALERT = 'PENDING'", con=connectToDigitalOcean())