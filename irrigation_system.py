import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
import customtkinter

def forward():
    meter_1 = ttk.Meter(
    metersize=250,
    padding=20,
    amounttotal=100,
    # arcrange=180,
    # arcoffset=-180,
    amountused=70,
    textright='%',
    subtext='Soil Moisture',
    bootstyle='info',
    interactive=True
    ).place(relx=0.5, rely=0.20, anchor='n')

def start():
    btn_labels_1 = ttk.Label(
        master=root,
        bootstyle = "sucess",
        text = "System is running...",
        width = 20,
        )
    btn_labels_1.place(relx=0.53, rely=0.92, anchor='center')

    progress = ttk.Progressbar(root, bootstyle = "striped",
            orient='horizontal', 
            length=500, mode='determinate')
    progress.place(relx=0.50, rely=0.95, anchor='center')

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    btn_labels_1.destroy()
    progress.destroy()
 
def stop():
    btn_labels_2 = ttk.Label(
        master=root,
        bootstyle = "sucess",
        text = "System shutdown...",
        width = 20,
        ).place(relx=0.53, rely=0.50, anchor='center')
    
    progress = ttk.Progressbar(root, bootstyle = "danger",
            orient='horizontal', 
            length=500, mode='determinate')
    progress.place(relx=0.50, rely=0.95, anchor='center')

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    progress.destroy()
    root.destroy()

root = tk.Tk()
root.title("Automatic Irrigation System")
root.geometry("300x500") #You want the size of the app to be 500x500
root.resizable(0, 0)
style = ttk.Style("superhero")

frame = ttk.Frame(master = root, width = 100, height = 450).pack()
title = ttk.Label( master=frame,
           font="-size 16",
           text= "Automatic Irrigation System",
           bootstyle = "light",
           ).place(relx = 0.5, anchor='n')



meter = ttk.Meter(
    metersize=250,
    padding=20,
    stripethickness=2,
    amountused=50,
    subtext='Water Capacity',
    textright='%',
    bootstyle='success',
    interactive=True
    ).place(relx=0.5, rely=0.20, anchor='n')


meter_1 = ttk.Meter(
    metersize=250,
    padding=20,
    amounttotal=100,
    # arcrange=180,
    # arcoffset=-180,
    amountused=70,
    textright='%',
    subtext='Soil Moisture',
    bootstyle='info',
    interactive=True
    ).place(relx=0.5, rely=0.20, anchor='n')


meter_2 = ttk.Meter(
    metersize=250,
    padding=20,
    amounttotal=280,
    # arcrange=180,
    # arcoffset=-180,
    stripethickness=10,              
    amountused=45,
    textright='°F',
    subtext='Temperature',
    wedgesize=5,
    bootstyle='info',
    interactive=True
    ).place(relx=0.5, rely=0.20, anchor='n')

btn_labels = ttk.Label( master=root,
           bootstyle = "sucess",
           ).pack(side = 'bottom')


button_on = customtkinter.CTkButton(master = btn_labels,width=40, height=40, corner_radius=40,
           text = "On",fg_color="#76BA1B", hover_color="#ACDF87",
            command = lambda: forward(),
           ).pack(side = 'left',padx=8, expand = 'true')

button_off = customtkinter.CTkButton(master = btn_labels,width=40, height=40, corner_radius=40,
           text = "Off",fg_color="#D35B58", hover_color="#C77C78",
           command = lambda: back(),
           ).pack(side = 'left', expand = 'true' )

root.mainloop()
