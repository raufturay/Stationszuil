import datetime
import psycopg2
conn = psycopg2.connect(
   dbname="Stationszuil", user='postgres', password='rauf', host='localhost')
c = conn.cursor()

def data_entry(name, date, station, bericht, goedkeuring, keurdatum, keurtijd, id):
    c.execute("INSERT INTO berichtenns (naam, datum, station, bericht,goedkeuring,goedkeuringdatum,goedkeuringtijd,moderatorid) VALUES(%s , %s,%s,%s,%s,%s,%s,%s)",(name, date, station, bericht,goedkeuring, keurdatum, keurtijd,id))
    # c.execute(f"INSERT INTO berichtenns (naam, datum, bericht, station,goedkeuring,goedkeuringdatum,goedkeuringtijd) VALUES('{name}', '{date}', '{station}', '{bericht}','{goedkeuring}', '{keurdatum}', '{keurtijd}');")





    conn.commit()




file = open("module1.csv")
lines = len(file.readlines())
file.close()

file = open("module1.csv", "r")

for line in file:
    totaal = line.strip().split(";")
    naam = totaal[0]
    print(naam)
    datum = totaal[1]
    print(datum)
    station = totaal[2]
    print(station)
    bericht = totaal[3]
    print(bericht)
    goedkeuring = input('keur je dit bericht goed: ')
    date = datetime.datetime.now()
    keurdatum = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
    keurtijd = date.time()
    moderatornaam = input('wat is je naam: ')
    moderatoremail = input('wat is je email: ')
    c.execute("SELECT email FROM moderatorns ")
    moderators = c.fetchall()

    for moderator in moderators:
        if moderator[0] == moderatoremail:
            c.execute("SELECT moderatorid FROM moderatorns WHERE email =  %s", [moderatoremail])
            id = c.fetchall()
            data_entry(naam, datum, station, bericht, goedkeuring, keurdatum, keurtijd, id[0])
            break
    else:
        c.execute("INSERT INTO moderatorns (naam, email) VALUES(%s,%s)", (moderatornaam, moderatoremail))

        c.execute("SELECT MAX(moderatorid) FROM moderatorns ")
        modid = c.fetchall()
        id = modid[0]
        id = id[0]
        data_entry(naam,datum,station,bericht,goedkeuring,keurdatum,keurtijd,id)

file.close()
with open("module1.csv",'r+') as file:
    file.truncate(0)