import tkinter as tk
from ctypes import windll
import requests
import json
import psycopg2
conn = psycopg2.connect(
   dbname="Stationszuil", user='postgres', password='rauf', host='localhost')
c = conn.cursor()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=52.092876&lon=5.104480&appid=8933246e2b0024f9c7e65dde3a317fbf")
for i in response:
   print(i)
root = tk.Tk()
root.title("module 3 GUI")
root.geometry("1100x850")
message = tk.Label(root, text="Berichten", font=('Arial',18))
message.pack(padx=20,pady=20)
c.execute("SELECT naam,datum,bericht FROM berichtenns order by datum asc fetch  first 5 rows only ")
berichten = c.fetchall()
for bericht in berichten:
   message = tk.Label(root, text=f"{bericht[0]} zegt op {bericht[1]}\n{bericht[2]}", font=('Arial', 12))
   message.pack(padx=20, pady=20)

c.execute("SELECT ovbike, elevator,toilet,par_and_ride FROM services WHERE station = 'alkmaar' ")
serviceslist = c.fetchall()
faciliteiten = ['ov-bike','elevator','toilet','park_and_ride']
for servicetuple in serviceslist:
   for service in servicetuple:
      for faciliteit in faciliteiten:
         if service == True:
            beschikbaar = "Ja"
            message = tk.Label(root, text=f"{faciliteit}\n{beschikbaar}",anchor='e', font=('Arial', 12))
            message.pack(padx=40, pady=40,fill='both')
         else:
            beschikbaar = "Nee"
            message = tk.Label(root, text=f"{faciliteit}\n{beschikbaar}",anchor='e', font=('Arial', 12))
            message.pack(padx=40, pady=40, fill='both' )
for weer in response:
   message = tk.Label(root, text=weer,anchor='center', font=('Arial',12))
   message.pack(fill='both' )


windll.shcore.SetProcessDpiAwareness(1)

root.mainloop()