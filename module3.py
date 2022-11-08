import tkinter as tk
from ctypes import windll
import requests
import json
import psycopg2
conn = psycopg2.connect(
   dbname="Stationszuil", user='postgres', password='rauf', host='localhost')
c = conn.cursor()


root = tk.Tk()
root.title("module 3 GUI")
root.geometry("1100x850")
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the station name and
# print facilities and weather on the screen
def submit():
   name_label.pack_forget()
   name_entry.pack_forget()
   sub_btn.pack_forget()
   global name
   name = name_var.get()

   response = requests.get(
      "https://api.openweathermap.org/data/2.5/weather?q=" + name + "&appid=8933246e2b0024f9c7e65dde3a317fbf")


   message = tk.Label(root, text="Berichten", font=('Arial',18))
   message.pack(padx=20,pady=20)
   c.execute("SELECT naam,datum,bericht FROM berichtenns Where goedkeuring = 'ja' order by datum asc fetch  first 5 rows only")
   berichten = c.fetchall()
   for bericht in berichten:
      message = tk.Label(root, relief="sunken" ,text=f"{bericht[0]} zegt op {bericht[1]}\n{bericht[2]}", font=('Arial', 12))
      message.pack(padx=20, pady=20)

   c.execute("SELECT ovbike, elevator,toilet,par_and_ride FROM services WHERE station = %s", [name])
   serviceslist = c.fetchone()
   faciliteiten = ('ov-bike','elevator','toilet','park_and_ride')
   print(serviceslist)
   services = tuple(zip(faciliteiten,serviceslist))
   print(services)
   for service_name,service_available in services:
      message = tk.Label(root, text=f"{service_name}  {service_available}\n", font=('Arial', 12))
      message.pack()


   for weer in response:
      message = tk.Label(root, text=weer, font=('Arial',12))
      message.pack()




# creating a label for
# name using widget Label
name_label = tk.Label(root, text='station', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.pack()
name_entry.pack()
sub_btn.pack()


#
#


windll.shcore.SetProcessDpiAwareness(1)

root.mainloop()