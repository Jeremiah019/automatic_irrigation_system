import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk
import customtkinter

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self, height = 350, width = 50)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Loading, StartPage, Page1, Page2, Page3, Page4):

			frame = F(container, self)

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
        tk.Frame.__init__(self, parent)

	# label of frame Layout 2
        label = ttk.Label(self, text ="Automatic Irrigation System", font = "-size 16")
		
	# putting the grid in its place by using
        # grid
        label.place(anchor = "center", relx = 0.5, rely = 0.20)

        label2 = ttk.Label(self)
        label2.place(anchor = "center", relx = 0.5, rely = 0.90)

        button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40, fg_color=("#76BA1B"), hover_color="#ACDF87",
                                                 text ="StartPage", command = lambda: controller.show_frame(StartPage))
        button.place(anchor = "center", relx = 0.5, rely = 0.80)

        
# second window frame page1
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Automatic Irrigation System", font = "-size 16")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
                
        label2 = ttk.Label(self)
        label2.place(anchor = "center", relx = 0.5, rely = 0.90)

        # btn_labels_1 = ttk.Label(master=label2, bootstyle = "sucess", text = "System is running...", width = 20)
        # btn_labels_1.place(relx=0.25, rely=0.50, anchor='center')

        # progress = ttk.Progressbar(label2, bootstyle = "striped", orient='horizontal', length=200, mode='determinate')
        # progress.place(relx=0.50, rely=0.50, anchor='center')

        # import time

        # progress['value'] = 20
        # label2.update_idletasks()
        # time.sleep(1)

        # progress['value'] = 40
        # label2.update_idletasks()
        # time.sleep(1)

        # progress['value'] = 50
        # label2.update_idletasks()
        # time.sleep(1)

        # progress['value'] = 60
        # self.update_idletasks()
        # time.sleep(1)

        # progress['value'] = 80
        # label2.update_idletasks()
        # time.sleep(1)

        # progress['value'] = 100
        # label2.update_idletasks()
        # btn_labels_1.destroy()
        # progress.destroy()

        label2 = ttk.Label(self)
        label2.place(anchor = "center", relx = 0.5, rely = 0.50)

        button1 = customtkinter.CTkButton(label2, text ="Temperature", width=100, height=100,command = lambda : controller.show_frame(Page1))
        button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", width=100, height=100,command = lambda : controller.show_frame(Page2))
        button3 = customtkinter.CTkButton(label2, text ="Humidity",width=100, height=100, command = lambda : controller.show_frame(Page3))
        button4 = customtkinter.CTkButton(label2, text ="Water Level",width=100, height=100, command = lambda : controller.show_frame(Page4))
                
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)
        button3.grid(row = 2, column = 1, padx = 10, pady = 10)
        button4.grid(row = 2, column = 2, padx = 10, pady = 10)
                
# second window frame page1

class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Temperature", font = "-size 16")
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		meter = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    stripethickness=2,
                    amountused=50,
                    subtext='Temperature',
                    textright='%',
                    bootstyle='success',
                    interactive=True
                    ).place(relx=0.5, rely=0.20, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)
	
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color="#76BA1B", hover_color="#ACDF87",
                                                 text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.place(anchor = "center", relx = 0.5, rely = 0.80)
		button1.grid(row = 1, column = 1)
		button2.grid(row = 1, column = 2)
		button3.grid(row = 2, column = 1)
		button4.grid(row = 2, column = 2)

# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Soil Moisture", font = "-size 16")
		label.grid(row = 0, column = 4, padx = 10, pady = 10)


		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
                    amountused=70,
                    textright='%',
                    subtext='Soil Moisture',
                    bootstyle='info',
                    interactive=True
                    ).place(relx=0.5, rely=0.20, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)
	
		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color="#76BA1B", hover_color="#ACDF87",
                                                 text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.place(anchor = "center", relx = 0.5, rely = 0.80)
		button1.grid(row = 1, column = 1)
		button2.grid(row = 1, column = 2)
		button3.grid(row = 2, column = 1)
		button4.grid(row = 2, column = 2)

# fourth window frame page2
class Page3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Humidity", font = "-size 16")
		label.grid(row = 0, column = 4, padx = 10, pady = 10)


		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
                    amountused=70,
                    textright='%',
                    subtext='Humidity',
                    bootstyle='info',
                    interactive=True
                    ).place(relx=0.5, rely=0.20, anchor='n')


		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)
	
		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color="#76BA1B", hover_color="#ACDF87",
                                                 text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.place(anchor = "center", relx = 0.5, rely = 0.80)
		button1.grid(row = 1, column = 1)
		button2.grid(row = 1, column = 2)
		button3.grid(row = 2, column = 1)
		button4.grid(row = 2, column = 2)

# fifth window frame page2
class Page4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Water Level", font = "-size 16")
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		meter_1 = ttk.Meter(self,
                    metersize=250,
                    padding=20,
                    amounttotal=100,
                    amountused=70,
                    textright='%',
                    subtext='Water Level',
                    bootstyle='info',
                    interactive=True
                    ).place(relx=0.5, rely=0.20, anchor='n')

		label2 = ttk.Label(self)
		label2.place(anchor = "center", relx = 0.5, rely = 0.90)
	
		# button to show frame 2 with text
		# layout2
		button = customtkinter.CTkButton(self, width=40, height=40, corner_radius=40,fg_color="#76BA1B", hover_color="#ACDF87",
                                                 text ="StartPage", command = lambda : controller.show_frame(StartPage))
		button1 = customtkinter.CTkButton(label2, text ="Temperature", command = lambda : controller.show_frame(Page1))
	
		button2 = customtkinter.CTkButton(label2, text ="Soil Moisture", command = lambda : controller.show_frame(Page2))

		button3 = customtkinter.CTkButton(label2, text ="Humidity", command = lambda : controller.show_frame(Page3))

		button4 = customtkinter.CTkButton(label2, text ="Water Level", command = lambda : controller.show_frame(Page4))

	
		# putting the button in its place by
		# using grid
		button.place(anchor = "center", relx = 0.5, rely = 0.80)
		button1.grid(row = 1, column = 1)
		button2.grid(row = 1, column = 2)
		button3.grid(row = 2, column = 1)
		button4.grid(row = 2, column = 2)


if __name__ == '__main__':

    root = tkinterApp()
    root.title("Automatic Irrigation System")
    root.geometry("300x500") #You want the size of the app to be 500x500
    root.resizable(0, 0)
    style = ttk.Style("superhero")
    
    root.mainloop()