import tkinter as tk
import ttkbootstrap as ttk
import time

root = tk.Tk()
style = ttk.Style("superhero")


title = ttk.Label( master=root,
           font="-size 32",
           text= "Automatic Irrigation System",
           bootstyle = "light",
           ).pack(pady = 5, padx = 5)

frame = ttk.Frame(master = root, width = 100, height = 200).pack()

meter_1 = ttk.Meter(
    metersize=180,
    padding=20,
    stripethickness=2,
    amountused=50,
    subtext='Water Capacity',
    textright='%',
    bootstyle='success',
    interactive=True
    ).place(relx=0.5, rely=0.40, anchor='center')

meter = ttk.Meter(master = frame,
    metersize=180,
    padding=20,
    amounttotal=100,
    arcrange=180,
    arcoffset=-180,
    amountused=70,
    textright='%',
    subtext='Soil Moisture',
    bootstyle='info',
    interactive=True
    ).pack(side = 'right')


meter = ttk.Meter(master = frame,
    metersize=180,
    padding=20,
    amounttotal=280,
    arcrange=180,
    arcoffset=-180,
    stripethickness=10,              
    amountused=45,
    textright='°F',
    subtext='Temperature',
    wedgesize=5,
    bootstyle='info',
    interactive=True
    ).pack(side = 'left')

btn_labels = ttk.Label( master=root,
           bootstyle = "sucess",
           ).pack(side = 'bottom')


button_on = ttk.Button(master = btn_labels,
           bootstyle="success",
           text = "On",
            command = lambda: start(),
           ).pack(side = 'left',padx=8, expand = 'true')

button_off = ttk.Button(master = btn_labels,
           bootstyle="danger",
           text = "Off",
           command = lambda: stop(),
           ).pack(side = 'left', expand = 'true' )

def start():
    btn_labels_1 = ttk.Label(
        master=root,
        bootstyle = "sucess",
        text = "Water is running...",
        width = 20,
        ).place(relx=0.54, rely=0.90, anchor='center')

    progress = ttk.Progressbar(master = root, bootstyle="striped", orient='horizontal', length=100, mode='indeterminate'
        ).place(relx=0.51, rely=0.95, anchor='center')
    progress.start(10)

def stop():
    btn_labels_2 = ttk.Label(
        master=root,
        bootstyle = "sucess",
        text = "Water is off",
        width = 20,
        ).place(relx=0.54, rely=0.90, anchor='center')

root.mainloop()
