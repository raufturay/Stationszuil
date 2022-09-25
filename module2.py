import sqlite3
import datetime
conn = sqlite3.connect('stationszuil.db')
c = conn.cursor()

file = open("module1.csv", "r")
read = file.read()
print(read)
file.close()
goedkeuring = input('keur je dit bericht goed: ')
date = datetime.datetime.now()
keurdatum = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
keurtijd = date.time()
moderatornaam = input('wat is je naam: ')
moderatoremail = input('wat is je email: ')


def data_entry():
    myfile = open("module1.csv", "r")
    name = myfile.readline(2)
    date = myfile.readline(3)
    station = myfile.readline(4)
    bericht = myfile.readline(5)
    myfile.close()
    c.execute("INSERT INTO berichten (Naam, Datum, Station, Bericht) VALUES(?, ?,?,?)",
              (name, date, station, bericht))
    c.execute("INSERT INTO beoordeling (Goedkeuring,Datum,Tijd) VALUES(?, ?,?)",
              (goedkeuring,keurdatum,keurtijd))
    c.execute("INSERT INTO moderator (Naam, Emailadres) VALUES(?, ?)",
              (moderatornaam,moderatoremail))

    conn.commit()