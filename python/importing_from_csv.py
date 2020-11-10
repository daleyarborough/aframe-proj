import sqlite3, csv

conn = sqlite3.connect('my_db.db')

cur = conn.cursor()

with open('./airbnb-dataset/AB_US_2020.csv', encoding="utf8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        name = row['name']
        price = row['price']
        city = row['city']


conn.commit()
conn.close()