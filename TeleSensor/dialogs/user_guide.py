import tkinter as tk
import ttkbootstrap as tkb
from PIL import Image
import customtkinter


# message box for help
class UserGuide:
    def __init__(self):
        self.window = tkb.Toplevel()
        self.window.title("User Guide")

        # set the window
        height = 400
        width = 428
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 3)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.resizable(False, False)
        self.window.scrollable_frame = tk.Frame(self.window)

        # adding image icon
        guide = customtkinter.CTkImage(light_image=Image.open("image/guide.png"),
                                       dark_image=Image.open("image/guide.png"), size=(26, 25))
        customtkinter.CTkLabel(self.window, text="", image=guide).place(x=137, y=16)

        tkb.Label(self.window, text="USER GUIDE", font=('Roboto', 16, 'underline', 'bold'),
                  style='info').place(x=167, y=20)
        # setting the instructions
        tkb.Label(self.window, text='LOADING FILE', font=('Roboto', 14, 'bold')).place(x=10, y=65)
        tkb.Label(self.window, text='The file accepted to calculate metrics must be .cvs file',
                  font=('Roboto', 13), wraplength=410, style='muted').place(x=17, y=87)

        tkb.Label(self.window, text='METRICS', font=('Roboto', 14, 'bold')).place(x=10, y=117)
        tkb.Label(self.window, text='If you prefer to run with metrics select the checkbox "Process by metric"',
                  font=('Roboto', 13), wraplength=410, style='muted').place(x=17, y=137)
