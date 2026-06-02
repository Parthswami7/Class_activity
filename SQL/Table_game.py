import pandas as pd
import sqlite3
"""#### **2. Connect with SQLite Database**"""
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')
tables = pd.read_sql("""SELECT name
                        FROM sqlite_master
                        WHERE type='table';""", conn)
print(tables)
teams = pd.read_sql("""SELECT *
                        FROM Team;""", conn)
print(teams)
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)
"""**Conclusion -**
- 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
- 3 columns with null values
"""
print(matches)
MI_wins = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7;""", conn)
print(MI_wins)
MI_S8_S9 = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7 and Season_Id IN (8,9);""", conn)
print(MI_S8_S9)
new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)
print(new_teams)
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin)
                        FROM Match;""", conn)
print(min_max_margin)
