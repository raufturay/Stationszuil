import datetime
import psycopg2
conn = psycopg2.connect(
   dbname="Stationszuil", user='postgres', password='rauf', host='localhost')
c = conn.cursor()

def data_entry(name, date, station, bericht, goedkeuring, keurdatum, keurtijd, id):
    c.execute("INSERT INTO berichtenns (naam, datum, bericht, station,goedkeuring,goedkeuringdatum,goedkeuringtijd,moderatorid) VALUES(%s , %s,%s,%s,%s,%s,%s,%s)",(name, date, station, bericht,goedkeuring, keurdatum, keurtijd,id))
    # c.execute(f"INSERT INTO berichtenns (naam, datum, bericht, station,goedkeuring,goedkeuringdatum,goedkeuringtijd) VALUES('{name}', '{date}', '{station}', '{bericht}','{goedkeuring}', '{keurdatum}', '{keurtijd}');")





    conn.commit()




file = open("module1.csv")
lines = len(file.readlines())
file.close()

file = open("module1.csv", "r")
for line in range(1,lines,4):

    naam = file.readlines(line)
    naam = naam[0].strip()
    print(naam)
    datum = file.readlines(line+1)
    datum = datum[0].strip()
    print(datum)
    station = file.readlines(line+2)
    station = station[0].strip()
    print(station)
    bericht = file.readlines(line+3)
    bericht = bericht[0].strip()
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
            print("1")
            break
    else:
        c.execute("INSERT INTO moderatorns (naam, email) VALUES(%s,%s)", (moderatornaam, moderatoremail))

        c.execute("SELECT MAX(moderatorid) FROM moderatorns ")
        modid = c.fetchall()
        id = modid[0]
        id = id[0]
        data_entry(naam,datum,station,bericht,goedkeuring,keurdatum,keurtijd,id)
        print("2")

file.close()