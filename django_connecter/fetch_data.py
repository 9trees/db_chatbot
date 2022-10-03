import sqlite3
import pandas as pd

import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('pythonsqlite.db')

df = pd.read_sql_query("SELECT * FROM polls_transformer", cnx)
