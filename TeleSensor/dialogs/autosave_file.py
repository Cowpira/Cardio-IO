import tkinter as tk
import ttkbootstrap as tkb
from PIL import Image
import customtkinter

# import from project
from save_result import SaveResult
from success_modal import SuccessDialog


# message box for help
class AutoSaveFile:
    def __init__(self):
        self.window = tkb.Toplevel()
        self.window.title("System Save Result")

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

        tkb.Label(self.window, text="File Auto Save", font=('Roboto', 23, 'bold'), style='info').place(x=169, y=35)

        # message label
        tkb.Label(self.window, text='The system will automatically save the PDF and CVS files into folder: '
                                    '"unnamedResults." \n Both files will be labeled with the current date.',
                  justify='center', font=('Roboto', 13), wraplength=410, style='primary').place(x=17, y=185)

        # button ok
        customtkinter.CTkButton(self.window, text='OK', width=100, height=48, compound="left", fg_color="#1976D2",
                                hover_color="#424242", font=('Roboto', 18), command=SuccessDialog).place(x=85, y=295)

        # button rename
        customtkinter.CTkButton(self.window, text='RENAME', width=100, height=48, compound="left",
                                fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                                command=SaveResult).place(x=235, y=295)
