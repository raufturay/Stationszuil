import tkinter as tk
from ctypes import windll
import requests
import json
import psycopg2
conn = psycopg2.connect(
   dbname="Stationszuil", user='postgres', password='rauf', host='localhost')
c = conn.cursor()

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=52.092876&lon=5.104480&appid=8933246e2b0024f9c7e65dde3a317fbf")
root = tk.Tk()
message = tk.Label(root, text=response.json())
message.pack()
windll.shcore.SetProcessDpiAwareness(1)

root.mainloop()