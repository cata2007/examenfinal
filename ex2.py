import pandas as pd
import sqlite3
conn = sqlite3.connect('db.sqlite3')
d=pd.read_sql_query("SELECT * from Users", conn)
print(d.head(4))
d["colnoua"] = d["first_name"].map(str) + d["last_name"]
print(d)
d.to_csv('test')
d.to_excel('test.xlsx')
dd=d['number_of_login'].mean
dd=d['number_of_login'].std