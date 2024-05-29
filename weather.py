from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get() #accessing the name of city through city_name
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=97ea69deadc2006e476c84a514d815b6").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])
    



win = Tk()
win.title("API by Kareem")
win.config(bg="light blue")
win.geometry("500x600")

name_label = Label(win,text="Weather Information App",font=("Helvetica",20,"bold"))
name_label.place(x=25,y=40,height=50,width=450)



city_name=StringVar()#getting the name of the city  in the city_name
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar",
"Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir",
"Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
"Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
"Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
"Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
"Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Weather Information App",values=list_name,
                   font=("Helvetica",15,"bold"),textvariable=city_name)
com.place(x=25,y=110,height=50,width=450)


done_button = Button(win,text="Submit",font=("Helvetica",15,"bold"))
done_button.place(x=200,y=180,height=50,width=100)

w_label = Label(win,text="Weather Climate",font=("Helvetica",15))
w_label.place(x=25,y=250,height=50,width=210)
w_label1 = Label(win,text="",font=("Helvetica",15))
w_label1.place(x=250,y=250,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("Helvetica",15))
wb_label.place(x=25,y=310,height=50,width=210)
wb_label1 = Label(win,text="",font=("Helvetica",15))
wb_label1.place(x=250,y=310,height=50,width=210) #to show values from api

temp_label = Label(win,text="Temperature",font=("Helvetica",15))
temp_label.place(x=25,y=370,height=50,width=210)
temp_label1 = Label(win,text="",font=("Helvetica",15))
temp_label1.place(x=250,y=370,height=50,width=210)

per_label = Label(win,text="Pressure",font=("Helvetica",15))
per_label.place(x=25,y=430,height=50,width=210)
per_label1 = Label(win,text="",font=("Helvetica",15))
per_label1.place(x=250,y=430,height=50,width=210)

done_button = Button(win,text="Submit",font=("Helvetica",15,"bold"),command=data_get)
done_button.place(x=200,y=180,height=50,width=100)

win.mainloop()