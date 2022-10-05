import datetime
import random
name = input('wat is je naam: ')
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

message = "\n"+ str(name) + "\n" + str(date.day) + '-' + str(date.month) + '-' + str(date.year)+ "\n" + str(random_station)+ "\n" + str(message)
f = open("module1.csv", "a")
f.write(message)
f.close()
