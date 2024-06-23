import sqlite3 as sq
import csv
import pandas as pd

conn = sq.connect('SpotifyDatabase.db')

cursor = conn.cursor()


spotidata = []

with open('present.csv', 'r', encoding='utf-8') as file:
    spotifile = csv.reader(file)
    for row in spotifile:
        spotidata.append(row)

print(spotidata)
df = pd.DataFrame(spotidata[1:], columns=spotidata[0])




