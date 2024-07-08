import tkinter as tk
import ttkbootstrap as tkb
from PIL import Image
import customtkinter


# message box for help
class SaveResult:
    def __init__(self):
        self.window = tkb.Toplevel()
        self.window.title("Save Result")

        # set the window
        height = 390
        width = 428
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 3)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.resizable(False, False)
        self.window.scrollable_frame = tk.Frame(self.window)

        # adding image icon
        save = customtkinter.CTkImage(light_image=Image.open("image/save-file.png"),
                                      dark_image=Image.open("image/save-file.png"), size=(32, 32))
        customtkinter.CTkLabel(self.window, text="", image=save).place(x=137, y=36)

        tkb.Label(self.window, text="Save File", font=('Roboto', 23, 'bold'), style='info').place(x=169, y=35)
        # setting the instructions
        tkb.Label(self.window, text='File Name:', font=('Roboto', 16)).place(x=65, y=95)
        tkb.Entry(self.window, width=30, font=('Roboto', 13)).place(x=65, y=117)

        tkb.Label(self.window, text='The PDF and CVS outputs will be saved into the folder with the same '
                                    'name specified above.', justify='center', font=('Roboto', 13),
                  wraplength=410, style='primary').place(x=17, y=185)

        # button save
        customtkinter.CTkButton(self.window, text='SAVE', width=100, height=48, compound="left",
                                fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18)).place(x=85, y=295)

        # button cancel
        customtkinter.CTkButton(self.window, text='CANCEL', width=100, height=48, compound="left",
                                fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18)).place(x=235, y=295)
