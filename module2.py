import sqlite3
import datetime
conn = sqlite3.connect('stationszuil.db')
c = conn.cursor()


def data_entry(name, date, station, bericht, goedkeuring, keurdatum, keurtijd, moderatornaam, moderatoremail):
    c.execute("INSERT INTO berichten (Naam, Datum, Station, Bericht) VALUES(?, ?,?,?)",
              (name, date, station, bericht))
    c.execute("INSERT INTO beoordeling (Goedkeuring,Datum,Tijd) VALUES(?, ?,?)",
              (goedkeuring, keurdatum, keurtijd))
    c.execute("INSERT INTO moderator (Naam, Emailadres) VALUES(?, ?)",
              (moderatornaam, moderatoremail))

    conn.commit()

file = open("module1.csv")
lines = len(file.readlines())
file.close()

file = open("module1.csv", "r")
for line in range(1,lines,4):
    naam = file.readlines(line)
    print(naam)
    datum = file.readlines(line+1)
    print(datum)
    station = file.readlines(line+2)
    print(station)
    bericht = file.readlines(line+3)
    print(bericht)
    goedkeuring = input('keur je dit bericht goed: ')
    date = datetime.datetime.now()
    keurdatum = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
    keurtijd = date.time()
    moderatornaam = input('wat is je naam: ')
    moderatoremail = input('wat is je email: ')
    data_entry(naam,datum,station,bericht,goedkeuring,keurdatum,keurtijd,moderatornaam,moderatoremail)

file.close()