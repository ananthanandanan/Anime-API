import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')
df = pd.read_csv('anime.csv')


df['id'] = df.index

df =df[['id','Anime_id', 'Name', 'Genre', 'Type', 'Episode', 'Rating', 'Members']]
df.to_sql('Anime_animemodel', conn, if_exists='replace', index=False)


cursor = conn.cursor()
cursor.execute("SELECT NAME FROM Anime_animemodel;")
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())