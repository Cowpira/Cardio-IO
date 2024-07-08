import tkinter as tk
import ttkbootstrap as tkb
from PIL import Image, ImageTk

# project imports
from dialogs.user_guide import UserGuide


class Search_Results:
    def __init__(self):
        self.window = tkb.Toplevel()
        self.window.title("Search Results")

        # set the window
        height = 500
        width = 680
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 3)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.resizable(False, False)

        # Styling my tkb elements
        tkb_style = tkb.Style()
        tkb_style.configure('primary.TButton', font=("Roboto", 20))

        # window header
        (tkb.Separator(self.window, orient='horizontal', style='secondary.Horizontal.TSeparator')
         .place(relx=0, rely=-0.387, relwidth=1, relheight=1))

        # logo
        logo = Image.open('image/logo.png').resize((143, 50))
        logo = ImageTk.PhotoImage(logo)
        tk.Label(self.window, image=logo).place(x=3, y=2)

        # search button
        tkb.Button(self.window, text=' Return', compound="left",
                   style='info.outline.TButton').place(x=570, y=9)

        tkb.Label(self.window, text="Review Process", font=('Roboto', 25)).place(x=250, y=70)

        def search_file():
            file = tk.filedialog.askopenfilename(title='Select file...',
                                                 filetypes=[("CVS file", "*.cvs"), ("XLSX file", "*.xlsx")])

            tkb.Label(self.window, style='dark', text='File selected: ' + str(format(file)), border=2, wraplength=420,
                      font=('Roboto', 13)).place(x=160, y=150)

        # method to search a file
        tkb.Label(self.window, text="Search Previews Result", font=('Roboto', 20)).place(x=45, y=118)

        # upload button
        upload = Image.open("image/upload.png").resize((17, 19))
        upload = ImageTk.PhotoImage(upload)
        (tkb.Button(self.window, text='SELECT FILE', image=upload, compound="left", style='info.outline.TButton',
                    command=lambda: search_file()).place(x=45, y=145))

        tkb.Button(self.window, text="REVIEW RESULT", width=13, style="primary.TButton").place(x=230, y=215)

        tkb.Label(self.window, text="Recent Results", font=('Roboto', 20)).place(x=45, y=265)

        # button for help
        help_icon = Image.open("image/helper.png").resize((20, 24))
        help_icon = ImageTk.PhotoImage(help_icon)
        tkb.Button(self.window, image=help_icon, style='info.TButton', command=UserGuide).place(x=630, y=455)