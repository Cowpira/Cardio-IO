import tkinter as tk
import ttkbootstrap as tkb
from PIL import Image
import customtkinter


# message box for help
class MetricsDesc:
    def __init__(self):
        self.window = tkb.Toplevel()
        self.window.title("Metrics Description")

        # set the window
        height = 400
        width = 428
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 3)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.resizable(False, False)
        self.window.scrollable_frame = tk.Frame(self.window)

        # adding image icon
        metric = customtkinter.CTkImage(light_image=Image.open("image/metrics.png"),
                                        dark_image=Image.open("image/metrics.png"), size=(26, 30))
        customtkinter.CTkLabel(self.window, text="", image=metric).place(x=138, y=13)

        tkb.Label(self.window, text="METRICS", font=('Roboto', 16, 'underline', 'bold'), style='info').place(x=170, y=20)

        # description about the metrics
        tkb.Label(self.window, text='The metrics calculated in this system will use the data from .CVS file(s) and '
                  'display the results in a graph.',
                  font=('Roboto', 13), wraplength=410, style='muted').place(x=17, y=67)
