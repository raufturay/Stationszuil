import datetime
import random

name = input('wat is je naam: ')
if name == '':
    name = 'Anoniem'
message = input('je feedback: ')
station = ['Arnhem', 'Utrecht', 'Alkmaar']
date = datetime.datetime.now()

if len(message) > 140:
    print('bericht te lang')
    message = input('je feedback: ')
random_station = random.choice(station)

print(name)
print(date.day , '-' , date.month , '-' , date.year)
print(random_station)
print(message)

message =  str(name) + ";" + str(date.day) + '-' + str(date.month) + '-' + str(date.year)+ ";" + str(random_station)+ ";" + str(message) + "\n"
f = open("module1.csv", "a")
f.write(message)
f.close()
