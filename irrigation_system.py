import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk
import customtkinter
from PIL import Image,ImageTk

LARGEFONT =("Arial", 35)

def turn_off():
	print("shutting down...")
	root.destroy()

class tkinterApp(tk.Tk):
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self, height = 350, width = 50)
		container.pack(side = "top", fill = "both", expand = True)
		container.configure(bg = '#FFFFFF')

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# self.label = {}

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Loading, StartPage, Page1, Page2, Page3, Page4):

			frame = F(container, self)
			frame.configure(bg = '#FFFFFF')

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(Loading)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage
class Loading(tk.Frame):  
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = "#FFFFFF")

	# label of frame Layout 2
        label = ttk.Label(self, text ="Automatic Irrigation System", font = "-size 16")
        label.place(anchor = "center", relx = 0.5, rely = 0.20)

        label2 = ttk.Label(self)
        label2.place(anchor = "center", relx = 0.5, rely = 0.90)

        photo = PhotoImage(file = r"C:\Users\callm\Documents\GitHub\automatic_irrigation_system\icons8-shutdown-24(-ldpi).png")

        button = customtkinter.CTkButton(self, width=40, height=40, image = photo, text = "On", corner_radius=40, fg_color=("#76BA1B"), hover_color="#ACDF87", command = lambda: controller.show_frame(StartPage))
        button.place(anchor = "center", relx = 0.5, rely = 0.50)
		
        button_1 = customtkinter.CTkButton(self, width=40, height=40, image = photo, text = "Off", corner_radius=40, fg_color=("#ff0000"), hover_color="#ff7b7b", command = lambda: turn_off())
        button_1.place(anchor = "center", relx = 0.5, rely = 0.60)

        
# second window frame page1
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Farm", font = "-size 16")
        label.place(anchor = "ne", relx = 0.50, rely = 0.04)

        switch = customtkinter.CTkSwitch(self, text="Wifi")
        switch.place(anchor = "nw", relx = 0.55, rely = 0.05)
                
        label2 = ttk.Label(self)
        label2.place(anchor = "center", relx = 0.5, rely = 0.90)

        label2 = ttk.Label(self, width=100)
        label2.place(anchor = "center", relx = 0.5, rely = 0.50)

        img = (Image.open("icons8-home-page-48.png"))

        resize1 = img.resize((40, 40), Image.LANCZOS)
        home = ImageTk.PhotoImage(resize1)	


        button = customtkinter.CTkButton(self, width=20, height=20, corner_radius=40,fg_color= "#FFFFFF", hover_color= "#7EC8E3",
                                                 text ="", image = home, command = lambda : controller.show_frame(Loading))

        icon_therm = PhotoImage(file = r"C:\Users\callm\Documents\GitHub\automatic_irrigation_system\thermometer_FILL0_wght400_GRAD0_opsz48.png")
        icon_waterl = PhotoImage(file = r"C:\Users\callm\Documents\GitHub\automatic_irrigation_system\water_FILL0_wght400_GRAD0_opsz48.png")
        icon_humi = PhotoImage(file = r"C:\Users\callm\Documents\GitHub\automatic_irrigation_system\humidity_mid_FILL0_wght400_GRAD0_opsz48.png")
        icon_moist = PhotoImage(file = r"C:\Users\callm\Documents\GitHub\automatic_irrigation_system\icons8-moisture-48.png")

        button1 = customtkinter.CTkButton(label2, image = icon_therm, text ="", fg_color= "#FFFFFF", hover_color= "#7EC8E3", width=100, height=100, command = lambda : controller.show_frame(Page1))
        button2 = customtkinter.CTkButton(label2, image = icon_moist, text ="", fg_color= "#FFFFFF", hover_color= "#7EC8E3",width=100, height=100, command = lambda : controller.show_frame(Page2))
        button3 = customtkinter.CTkButton(label2, image = icon_humi, text ="",fg_color= "#FFFFFF",hover_color= "#7EC8E3",width=100, height=100, command = lambda : controller.show_frame(Page3))
        button4 = customtkinter.CTkButton(label2, image = icon_waterl, text ="",fg_color= "#FFFFFF",hover_color= "#7EC8E3",width=100, height=100, command = lambda : controller.show_frame(Page4))

        separator1 = ttk.Label(label2, text = "Temperature")
        # separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
        
        separator2 = ttk.Label(label2, text = "Soil Moisture")
        # separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
        
        separator3 = ttk.Label(label2,text = "Humidity")
        # separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
        
        separator4 = ttk.Label(label2,text = "Water Level")
        # separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
        

        button.grid(row = 2, column = 0	, padx = 5, pady=12)
        button1.grid(row = 1, column = 1, padx = 10, pady = 5)
        separator1.grid(row = 2, column = 1, padx = 10)
        button2.grid(row = 1, column = 2, padx = 10, pady = 5)
        separator2.grid(row = 2, column = 2, padx = 10, pady = 5)
        button3.grid(row = 3, column = 1, padx = 10, pady = 5)
        separator3.grid(row = 4, column = 1, padx = 10, pady = 5)
        button4.grid(row = 3, column = 2, padx = 10, pady = 5)
        separator4.grid(row = 4, column = 2, padx = 10, pady = 5)
        


                
# second window frame page1

class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Temperature", font = "-size 16")
		label.place(anchor = "center", relx = 0.5, rely = 0.05)

		meter = ttk.Meter(self,
                    metersize=250,
					amounttotal=100,
                    padding=20,
                    stripethickness=2,
                    amountused=50,
                    subtext='Temperature',
                    textright='°C',
                    bootstyle='success',
                    interactive=True
                    ).place(relx=0.5, rely=0.15, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)

		img = (Image.open("icons8-home-page-48.png"))

		resize1 = img.resize((40, 40), Image.LANCZOS)
		home = ImageTk.PhotoImage(resize1)	


		button = customtkinter.CTkButton(self, width=20, height=20, corner_radius=40,fg_color= "#FFFFFF", hover_color= "#7EC8E3",
                                                 text ="", image = home, command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture",fg_color= "#FFFFFF", hover_color= "#7EC8E3", command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity",fg_color= "#FFFFFF", hover_color= "#7EC8E3", command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.grid(row = 0, column = 0	, padx = 5, pady=5)
		button1.grid(row = 1, column = 1, padx = 5, pady=5)
		button2.grid(row = 1, column = 2, padx = 5, pady=5)
		button3.grid(row = 2, column = 1, padx = 5, pady=5)
		button4.grid(row = 2, column = 2, padx = 5, pady=5)

# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Soil Moisture", font = "-size 16")
		label.place(anchor = "center", relx = 0.5, rely = 0.05)


		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
					stripethickness=2,
                    amountused=70,
                    textright='%',
                    subtext='Soil Moisture',
                    bootstyle='info',
                    interactive=True
                    ).place(relx=0.5, rely=0.15, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)

		img = Image.open("icons8-home-page-48.png")

		resize1 = img.resize((40, 40), Image.LANCZOS)
		home = ImageTk.PhotoImage(resize1)	
	
		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color= "#FFFFFF", hover_color= "#7EC8E3",
                                                 text ="", image = home, command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level",fg_color= "#FFFFFF", hover_color= "#7EC8E3", command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.grid(row = 0, column = 0	, padx = 5, pady=5)
		button1.grid(row = 1, column = 1, padx = 5, pady=5)
		button2.grid(row = 1, column = 2, padx = 5, pady=5)
		button3.grid(row = 2, column = 1, padx = 5, pady=5)
		button4.grid(row = 2, column = 2, padx = 5, pady=5)

# fourth window frame page2
class Page3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Humidity", font = "-size 16")
		label.place(anchor = "center", relx = 0.5, rely = 0.05)


		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
					stripethickness=2,
                    amountused=45,
                    textright='%',
                    subtext='Humidity',
                    bootstyle='danger',
                    interactive=True
                    ).place(relx=0.5, rely=0.15, anchor='n')


		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)

		img = Image.open("icons8-home-page-48.png")

		resize1 = img.resize((40, 40), Image.LANCZOS)
		home = ImageTk.PhotoImage(resize1)	

		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color= "#FFFFFF", hover_color= "#7EC8E3",
                                                 text ="", image = home, command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.grid(row = 0, column = 0	, padx = 5, pady=5)
		button1.grid(row = 1, column = 1, padx = 5, pady=5)
		button2.grid(row = 1, column = 2, padx = 5, pady=5)
		button3.grid(row = 2, column = 1, padx = 5, pady=5)
		button4.grid(row = 2, column = 2, padx = 5, pady=5)

# fifth window frame page2
class Page4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Water Level", font = "-size 16")
		label.place(anchor = "center", relx = 0.5, rely = 0.05)

		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
					stripethickness=2,
                    amountused=90,
                    textright='%',
                    subtext='Water Level',
                    bootstyle='primary',
                    interactive=True
                    ).place(relx=0.5, rely=0.15, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)

		img = Image.open("icons8-home-page-48.png")

		resize1 = img.resize((40, 40), Image.LANCZOS)
		home = ImageTk.PhotoImage(resize1)	

		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color= "#FFFFFF", hover_color= "#7EC8E3",
                                                 text ="", image = home, command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature",fg_color= "#FFFFFF", hover_color= "#7EC8E3", command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", fg_color= "#FFFFFF", hover_color= "#7EC8E3",command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level",fg_color= "#FFFFFF", hover_color= "#7EC8E3", command = lambda : controller.show_frame(Page4))

		

	
		# putting the button in its place by
		# using grid
		button.grid(row = 0, column = 0	, padx = 5, pady=5)
		button1.grid(row = 1, column = 1, padx = 5, pady=5)
		button2.grid(row = 1, column = 2, padx = 5, pady=5)
		button3.grid(row = 2, column = 1, padx = 5, pady=5)
		button4.grid(row = 2, column = 2, padx = 5, pady=5)


if __name__ == '__main__':

    root = tkinterApp()
    root.title("Automatic Irrigation System")
    root.geometry("300x500")
    root.resizable(0, 0)

    

    root.mainloop()