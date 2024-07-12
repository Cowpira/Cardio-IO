"""
    Institution='UTD (University of Texas Dallas)',
    Course='CS4485 - Project',
    Professor='Miguel Razo-Razo',
    Company='Tele Sensor (Cardio IO)',
    Responsible='Sajol Ghoshal, Wayne Hohman, Steven Smith',
    Project='Cardio IO Heart Rate Metrics comparison',
    Version='0.1',
    Github_url='https://github.com/Cowpira/Cardio-IO',
    Download_url='https://drive.google.com/drive/folders/1FAux5hlM9ubSIHf9YSaKAq3JJ6GP7lWH?exids=71471483,71471477',
    License='TeleSensor',
    Authors='Raad Ahammad, Tamer Alaeddin, Nathaniel Faust, Nora Hanna, Celio Kelly, Joseph Saber',
    Description='GUI for the Cardio IO heart rate monitor.',
    Started='July 2, 2024',
    Delivered='yet in development'
"""
######################################################################################################
# packages & frameworks imports
import os
import tkinter as tk
from tkinter import END
import customtkinter
import ttkbootstrap as tkb
from PIL import Image
from tkinter.filedialog import askopenfile

# project imports
from dialogs.metrics_desc import MetricsDesc
from dialogs.user_guide import UserGuide
######################################################################################################


#######################################################################################################
# <region desc="setting windows home_page, search_page & result_page">
window = tkb.Window(themename='flatly')
window.title("Tele Sensor")

# set the window
main_x = (window.winfo_screenwidth() // 2) - (680 // 2)
main_y = (window.winfo_screenheight() // 2) - (500 // 3)
window.geometry('{}x{}+{}+{}'.format(680, 500, main_x, main_y))
window.resizable(False, False)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="setting dialog for save_result & autosave">
def set_dialog_window(dialog_frame):
    # set the window
    x = (dialog_frame.winfo_screenwidth() // 2) - (428 // 2)
    y = (dialog_frame.winfo_screenheight() // 2) - (390 // 3)
    dialog_frame.geometry('{}x{}+{}+{}'.format(428, 390, x, y))
    dialog_frame.resizable(False, False)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="setting dialog for success_dialog, fail_dialog & print_dialog">
def sett_dialog_window(dialog_frame):
    # set the window
    x = (dialog_frame.winfo_screenwidth() // 2) - (428 // 2)
    y = (dialog_frame.winfo_screenheight() // 2) - (270 // 3)
    dialog_frame.geometry('{}x{}+{}+{}'.format(428, 270, x, y))
    dialog_frame.resizable(False, False)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="styling elements">
tkb_style = tkb.Style()
tkb_style.configure('primary.TButton', font=("Roboto", 23))
tkb_style.configure('TCheckbutton', font=("Roboto", 25))
tkb_style.configure('secondary.Treeview', rowheight=25)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="shared images">
upload_btn = customtkinter.CTkImage(light_image=Image.open("image/upload.png"),
                                    dark_image=Image.open("image/upload.png"), size=(25, 25))
helper = customtkinter.CTkImage(light_image=Image.open("image/manual.png"),
                                dark_image=Image.open("image/manual.png"), size=(25, 25))

eye = customtkinter.CTkImage(light_image=Image.open("image/eye.png"),
                             dark_image=Image.open("image/eye.png"), size=(18, 18))
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="switching pages">
def switch_pages(page):
    for frame in main_frame.winfo_children():
        frame.destroy()
        window.update()

    page()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="getting all CSV files from a directory/ sub-directory">
def get_all_csv(data_store):
    for path, subdir, files in os.walk("Patient_Library"):
        for file in files:
            if file.endswith(".csv"):
                data_store.append(file)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="menu_frame">
menu = tkb.Frame(window, borderwidth=1, style='TLabelframe')
menu.configure(width=680, height=50)

# logo
logo = customtkinter.CTkImage(light_image=Image.open("image/logo.png"),
                              dark_image=Image.open("image/logo.png"), size=(153, 47))
customtkinter.CTkLabel(menu, text="", image=logo).place(x=0, y=0)

menu.pack_propagate(False)
menu.pack()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="main_frame">
main_frame = tkb.Frame(window)
main_frame.pack(fill=tkb.BOTH, expand=True)

# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="return_page_button">
def return_page():
    # search button
    return_btn = customtkinter.CTkImage(light_image=Image.open("image/return.png"),
                                        dark_image=Image.open("image/return.png"), size=(21, 21))
    customtkinter.CTkButton(menu, image=return_btn, text='Return ', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: switch_pages(page=home_page)).place(x=578, y=6)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="masking buttons">
# mak button return on processing screen
def masking_button():
    customtkinter.CTkButton(menu, text='', width=95, height=40,
                            fg_color="#FFFFFF", state='disabled').place(x=570, y=6)


# mak button return on processing screen
def masking_buttons():
    # mak button return on processing screen
    customtkinter.CTkButton(menu, text='', width=170, height=40,
                            fg_color="#FFFFFF", state='disabled').place(x=406, y=5)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="home_page_frame">
def home_page():
    home_frame = tkb.Frame(main_frame)
    masking_buttons()

    # search button
    search_btn = customtkinter.CTkImage(light_image=Image.open("image/search.png"),
                                        dark_image=Image.open("image/search.png"), size=(22, 22))
    customtkinter.CTkButton(menu, image=search_btn, text='Search', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: switch_pages(page=search_page)).place(x=578, y=6)

    # method to upload a file
    tkb.Label(home_frame, text="Select file(s)", font=('Roboto', 25)).place(x=130, y=10)
    tkb.Label(home_frame, text="File accepted .CSV", foreground='#424242', font=('Roboto', 12)).place(x=130, y=255)

    # getting all CSV files from directory and subdirectories
    # NOTE: the code still loading files from local directory 'Patient_Library'
    csv_file_list = []
    get_all_csv(csv_file_list)

    # list all CSV files into listbox
    list_items = tk.Listbox(home_frame, selectmode="multiple", width=50, font=('Arial', 13), border=4,
                            selectborderwidth=2)
    list_items.place(x=130, y=45)

    # listing all files into the listbox
    for each_item in range(len(csv_file_list)):
        list_items.insert(END, csv_file_list[each_item])
        list_items.itemconfigure(each_item, selectbackground='#4CAF50')

    cbx_state = tk.IntVar()

    def select_all():
        print(cbx_state.get())
        if cbx_state.get():
            list_items.select_set(0, END)
        else:
            list_items.select_clear(0, END)

    # button to select all items once
    select_all_cbx = customtkinter.CTkCheckBox(home_frame, text="Select All", font=('Roboto', 12), width=10, height=6,
                                               hover_color="#424242", fg_color='#4CAF50', text_color="#212121",
                                               variable=cbx_state, command=select_all)
    select_all_cbx.place(x=455, y=257)

    tkb.Button(home_frame, text="Click to learn more", style='primary.link.TButton',
               command=MetricsDesc).place(x=150, y=318)

    customtkinter.CTkCheckBox(master=home_frame, text="Process by metrics", width=25, height=25, font=("Roboto", 22),
                              fg_color="#4CAF50", hover_color="#424242", text_color="#212121").place(x=130, y=295)

    customtkinter.CTkButton(home_frame, text='PROCESS', width=170, height=48, fg_color="#1976D2", hover_color="#424242",
                            font=('Roboto', 18), command=lambda: switch_pages(page=processing_page)).place(x=250, y=358)

    # button for help
    customtkinter.CTkButton(home_frame, image=helper, text='', width=29, height=32, compound="left", fg_color="#FFFFFF",
                            hover_color="#424242", corner_radius=5, command=UserGuide).place(x=638, y=408)

    home_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="search_page_frame">
def search_page():
    search_frame = tkb.Frame(main_frame)
    masking_buttons()
    return_page()

    tkb.Label(search_frame, text="Review Process", font=('Roboto', 25)).place(x=250, y=8)
    # method to search a file
    tkb.Label(search_frame, text="Search Previews Result", font=('Roboto', 20)).place(x=75, y=55)

    # method to upload file
    def search_file():
        file = tk.filedialog.askopenfilename(title='Select file...',
                                             filetypes=[("CSV file", "*.csv"), ("XLSX file", "*.xlsx")])

        tkb.Label(search_frame, style='dark', text='File selected: ' + str(format(file)), border=2, wraplength=420,
                  font=('Roboto', 13)).place(x=242, y=94)

    # upload button
    customtkinter.CTkButton(search_frame, image=upload_btn, text='SELECT FILE', width=50, height=40, compound="left",
                            fg_color="#424242", hover_color="#90A4AE", corner_radius=24,
                            command=lambda: search_file()).place(x=85, y=83)

    tkb.Label(search_frame, text="File accepted .CSV", font=('Roboto', 13)).place(x=90, y=129)

    customtkinter.CTkButton(search_frame, text='REVIEW RESULT', width=170, height=48, fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: switch_pages(page=result_page)).place(x=250, y=155)

    # recent results panel
    recent_tab = customtkinter.CTkTabview(search_frame, width=610, height=200, corner_radius=12, fg_color="#EEEEEE")
    recent_tab.place(x=25, y=202)

    # list last 9 recent results
    tkb.Label(search_frame, text="Recent Results", foreground="#01579B", background="#EEEEEE",
              font=('Roboto', 23)).place(x=255, y=225)

    # calling function to design the table
    recent_result_table(search_frame)

    # adding legend to buttons success & fail
    customtkinter.CTkButton(search_frame, image=eye, text='', width=20, height=22, compound="left", fg_color="#81C784",
                            state='disabled', corner_radius=5).place(x=35, y=412)
    tkb.Label(search_frame, text="Succeed", style="dark").place(x=72, y=414)

    customtkinter.CTkButton(search_frame, image=eye, text='', width=30, height=22, compound="left", fg_color="#E57373",
                            state='disabled', corner_radius=5).place(x=194, y=412)
    tkb.Label(search_frame, text="Failed", style="dark").place(x=232, y=414)

    # button for help
    customtkinter.CTkButton(main_frame, image=helper, text='', width=29, height=32, compound="left", fg_color="#FFFFFF",
                            hover_color="#424242", corner_radius=5, command=UserGuide).place(x=638, y=408)

    search_frame.pack(fill=tkb.BOTH, expand=True)

# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="result_page_frame">
def result_page():
    result_frame = tkb.Frame(main_frame)
    return_page()

    # buttons from menu
    # save result button
    save_btn = customtkinter.CTkImage(light_image=Image.open("image/save.png"), dark_image=Image.open("image/save.png"),
                                      size=(22, 22))
    customtkinter.CTkButton(menu, image=save_btn, text=' Save ', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: save_result()).place(x=414, y=6)

    # print result button
    print_btn = customtkinter.CTkImage(light_image=Image.open("image/printer.png"),
                                       dark_image=Image.open("image/printer.png"), size=(22, 22))
    customtkinter.CTkButton(menu, image=print_btn, text='Print ', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: print_dialog()).place(x=498, y=6)

    # return to list button
    list_result = customtkinter.CTkImage(light_image=Image.open("image/result_list.png"),
                                         dark_image=Image.open("image/result_list.png"), size=(20, 20))
    customtkinter.CTkButton(menu, image=list_result, text='Results', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: switch_pages(page=search_page)).place(x=578, y=6)

    # function to list clients into the slider
    clients = ["John Rave", "Wanda Smith", "Steve Long", "Simone Cole", "Shawn Pat", "Sarah Jones", 'Mark Paul',
               'Ray Allen', 'Maria Hall']

    def list_result(value):
        lbl_result.configure(text=value + ' Result')

    # adding scroll to the slide bar
    x_scroll = tk.Scrollbar(result_frame, orient=tk.HORIZONTAL)
    x_scroll.place(x=0, y=0)

    # slide bar
    # slide_bar = customtkinter.CTkTabview(result_frame, width=680, height=61)
    slide_bar = tk.Listbox(result_frame, width=680, height=2, xscrollcommand=x_scroll.set)
    slide_bar.place(x=0, y=0)

    customtkinter.CTkSegmentedButton(slide_bar,  values=clients, font=('Roboto', 14), width=80, fg_color='#616161',
                                     selected_color='#4CAF50', unselected_hover_color='#212121', corner_radius=0,
                                     selected_hover_color='#212121', unselected_color='#616161',
                                     command=list_result).place(x=15, y=3)

    x_scroll.config(command=slide_bar.xview)

    """# adding navigation to tabview
    left = customtkinter.CTkImage(light_image=Image.open("image/left.png"),
                                  dark_image=Image.open("image/left.png"), size=(24, 24))
    customtkinter.CTkButton(slide_bar, image=left, text='', width=20, height=40, compound="left", fg_color="#212121",
                            hover_color='#BDBDBD', corner_radius=0, ).place(x=0, y=0)

    right = customtkinter.CTkImage(light_image=Image.open("image/next.png"),
                                   dark_image=Image.open("image/next.png"), size=(24, 24))
    customtkinter.CTkButton(slide_bar, image=right, text='', width=30, height=40, compound="left", fg_color="#212121",
                            hover_color='#BDBDBD', corner_radius=0).place(x=647, y=0)"""

    # recent results panel
    recent_tab = customtkinter.CTkTabview(result_frame, width=600, height=165, corner_radius=12, fg_color="#EEEEEE",
                                          border_color='red')
    recent_tab.place(x=35, y=40)

    lbl_result = customtkinter.CTkButton(result_frame, text='RESULT', width=160, height=33, fg_color="#4CAF50",
                                         font=('Roboto', 18, 'bold'), state='disable')
    lbl_result.place(x=260, y=48)

    # adding labels from result
    tkb.Label(result_frame, text="Date: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=50, y=98)
    tkb.Label(result_frame, text="March 7, 2024", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=88, y=98)

    tkb.Label(result_frame, text="Heart Rate: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=260, y=98)
    tkb.Label(result_frame, text="84", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=339, y=98)

    tkb.Label(result_frame, text="Metric: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=482, y=98)
    tkb.Label(result_frame, text="Bpm", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=531, y=98)

    tkb.Label(result_frame, text="RMS Value:", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=50, y=150)
    tkb.Label(result_frame, text="103.06", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=130, y=150)

    tkb.Label(result_frame, text="RMS Accuracy: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=260, y=150)
    tkb.Label(result_frame, text="88%", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=366, y=150)

    tkb.Label(result_frame, text="RMS Error: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=482, y=150)
    tkb.Label(result_frame, text="3%", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=558, y=150)

    # heart rate graph result
    rate_result = customtkinter.CTkImage(light_image=Image.open("image/heart_rate_result.png"),
                                         dark_image=Image.open("image/heart_rate_result.png"), size=(225, 225))
    customtkinter.CTkLabel(result_frame, text="", image=rate_result).place(x=240, y=215)

    result_frame.pack(fill=tkb.BOTH, expand=True)

# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="save_result">
def save_result():
    save_frame = tkb.Frame(main_frame)

    save_frame = tkb.Toplevel()
    save_frame.title("Save Result")
    set_dialog_window(save_frame)

    # adding image icon
    save = customtkinter.CTkImage(light_image=Image.open("image/save-file.png"),
                                  dark_image=Image.open("image/save-file.png"), size=(32, 32))
    customtkinter.CTkLabel(save_frame, text="", image=save).place(x=137, y=36)

    tkb.Label(save_frame, text="Save File", font=('Roboto', 23, 'bold'), style='info').place(x=171, y=35)
    # setting the instructions
    tkb.Label(save_frame, text='File Name:', font=('Roboto', 16)).place(x=67, y=93)
    tkb.Entry(save_frame, width=30, font=('Roboto', 13)).place(x=67, y=115)

    # recent results panel
    info_tab = customtkinter.CTkTabview(save_frame, width=365, height=115, corner_radius=12, fg_color="#EEEEEE")
    info_tab.place(x=25, y=152)
    tkb.Label(save_frame, text='The PDF and CSV files will be saved inside "TeleSensor_Results" folder. '
                               'Both will be named as specified by the user.', justify='center', font=('Roboto', 13),
              wraplength=355, background='#EEEEEE').place(x=46, y=190)

    # button save
    customtkinter.CTkButton(save_frame, text='SAVE', width=100, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: success_dialog(save_frame)).place(x=85, y=295)

    # button cancel
    customtkinter.CTkButton(save_frame, text='CANCEL', width=100, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: autosave(save_frame)).place(x=235, y=295)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="save_result">
def autosave(frame_caller):
    autosave_frame = tkb.Frame(main_frame)

    autosave_frame = tkb.Toplevel()
    autosave_frame.title("Autosave Result")
    set_dialog_window(autosave_frame)

    # adding image icon
    warning = customtkinter.CTkImage(light_image=Image.open("image/warning.png"),
                                     dark_image=Image.open("image/warning.png"), size=(60, 60))
    customtkinter.CTkLabel(autosave_frame, text="", image=warning).place(x=175, y=12)

    tkb.Label(autosave_frame, text="Autosave File", font=('Roboto', 23)).place(x=144, y=80)

    # recent results panel
    info_tab = customtkinter.CTkTabview(autosave_frame, width=350, height=135, corner_radius=12, fg_color="#FAE496")
    info_tab.place(x=40, y=118)
    tkb.Label(autosave_frame, text='The system will automatically save a PDF and CSV files into a folder '
                                   '"unnamedResults."\n\n Both will be labeled with the current date.',
              justify='center', font=('Roboto', 14), background="#FAE496", wraplength=320).place(x=65, y=158)

    # button save
    customtkinter.CTkButton(autosave_frame, text='OK', width=100, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: success_dialog(autosave_frame)).place(x=85, y=295)

    # button cancel
    customtkinter.CTkButton(autosave_frame, text='RENAME', width=100, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: switch_dialog(autosave_frame)).place(x=235, y=295)

    frame_caller.destroy()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="success dialog">
def success_dialog(frame_caller):
    success_frame = tkb.Frame(main_frame)

    success_frame = tkb.Toplevel()
    success_frame.title("Saved Successfully")
    sett_dialog_window(success_frame)

    # adding image icon
    success_icon = customtkinter.CTkImage(light_image=Image.open("image/success.png"),
                                          dark_image=Image.open("image/success.png"), size=(85, 85))
    customtkinter.CTkLabel(success_frame, text="", image=success_icon).place(x=170, y=20)

    # message label
    tkb.Label(success_frame, text='File saved successfully!', justify='center',
              font=('Roboto', 17, 'bold'), foreground='#212121').place(x=120, y=130)

    # button save
    customtkinter.CTkButton(success_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: success_frame.destroy()).place(x=165, y=190)
    frame_caller.destroy()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="fail dialog">
def fail_dialog(frame_caller):
    fail_frame = tkb.Frame(main_frame)

    fail_frame = tkb.Toplevel()
    fail_frame.title("Failed to Save")
    sett_dialog_window(fail_frame)

    # adding image icon
    fail_icon = customtkinter.CTkImage(light_image=Image.open("image/fail.png"),
                                       dark_image=Image.open("image/fail.png"), size=(85, 85))
    customtkinter.CTkLabel(fail_frame, text="", image=fail_icon).place(x=170, y=20)

    # message label
    tkb.Label(fail_frame, text='File could not be saved or already exist! \n Try again', justify='center',
              font=('Roboto', 17, 'bold'), foreground='#212121').place(x=47, y=125)

    # button save
    customtkinter.CTkButton(fail_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: fail_frame.destroy()).place(x=165, y=190)
    frame_caller.destroy()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="success dialog">
def print_dialog():
    print_frame = tkb.Frame(main_frame)

    print_frame = tkb.Toplevel()
    print_frame.title("Printing File")
    sett_dialog_window(print_frame)

    # adding image icon
    success_icon = customtkinter.CTkImage(light_image=Image.open("image/printing.png"),
                                          dark_image=Image.open("image/printing.png"), size=(85, 85))
    customtkinter.CTkLabel(print_frame, text="", image=success_icon).place(x=170, y=20)

    # printing progress
    tkb.Label(print_frame, text='Printing result', justify='center',
              font=('Roboto', 23), foreground='#212121').place(x=135, y=120)

    # button to close popup
    customtkinter.CTkButton(print_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: print_frame.destroy()).place(x=165, y=190)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="processing_page_frame">
def processing_page():
    processing_frame = tkb.Frame(main_frame)
    masking_button()
    masking_buttons()

    tkb.Label(processing_frame, text="Processing...", font=('Roboto', 25)).place(x=280, y=4)

    # adding image icon
    heart_rate = customtkinter.CTkImage(light_image=Image.open("image/heart_rate.gif"),
                                        dark_image=Image.open("image/heart_rate.gif"), size=(575, 260))
    customtkinter.CTkLabel(processing_frame, text="", image=heart_rate).place(x=50, y=45)

    tkb.Button(processing_frame, text="Graph details here", style='primary.link.TButton',
               command=MetricsDesc).place(x=40, y=305)

    # adding legend to heart rate waves CGI & HR
    hr = customtkinter.CTkImage(light_image=Image.open("image/hr.png"), dark_image=Image.open("image/hr.png"),
                                size=(22, 22))
    customtkinter.CTkButton(processing_frame, image=hr, text='', width=18, height=20, compound="left",
                            fg_color="#000000", state='disabled', corner_radius=5).place(x=472, y=313)
    tkb.Label(processing_frame, text="HR", style="dark").place(x=510, y=316)

    cgi = customtkinter.CTkImage(light_image=Image.open("image/cgi.png"), dark_image=Image.open("image/cgi.png"),
                                 size=(22, 22))
    customtkinter.CTkButton(processing_frame, image=cgi, text='', width=18, height=20, compound="left",
                            fg_color="#000000", state='disabled', corner_radius=5).place(x=555, y=313)
    tkb.Label(processing_frame, text="CGI", style="dark").place(x=592, y=316)

    # button for help
    customtkinter.CTkButton(processing_frame, text='STOP', width=170, height=48, fg_color="#EF5350",
                            hover_color="#424242", font=('Roboto', 18, 'bold'), corner_radius=5,
                            command=lambda: switch_pages(page=home_page)).place(x=245, y=355)

    processing_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="recent_results table">
def recent_result_table(search_frame):
    clients = [["John Rave"], ["Wanda Smith"], ["Steve Long"], ["Simone cole"], ["Shawn Pat"], ["Sarah Jones"],
               ['Mark Paul'], ['Ray Allen'], ['Maria Hall']]
    status = [['success'], ['fail'], ['fail'], ['success'], ['success'], ['fail'], ['fail'], ['fail'], ['success']]

    posix = 85
    col1 = 270
    col2 = 270
    col3 = 270

    for n in range(0, 9):
        # success button
        success_btn = customtkinter.CTkButton(search_frame, image=eye, text='', width=20, height=22, compound="left",
                                              fg_color="#81C784", hover_color="#90A4AE", corner_radius=5,
                                              command=lambda: switch_pages(page=result_page))
        # fail button
        fail_btn = customtkinter.CTkButton(search_frame, image=eye, text='', width=30, height=22, compound="left",
                                           fg_color="#E57373", hover_color="#90A4AE", corner_radius=5,
                                           command=lambda: switch_pages(page=result_page))

        client_name = tkb.Label(search_frame, foreground='#01579B', background="#EEEEEE", font=('Roboto', 14))

        if n <= 2:
            if status[n][0] == 'success':
                success_btn.place(x=posix + 110, y=col1)
            else:
                fail_btn.place(x=posix + 110, y=col1)

            client_name.config(text=clients[n][0])
            client_name.place(x=posix, y=col1 + 4)

            col1 += 40
        elif n <= 5:
            if status[n][0] == 'success':
                success_btn.place(x=posix + 285, y=col2)
            else:
                fail_btn.place(x=posix + 285, y=col2)

            client_name.config(text=clients[n][0])
            client_name.place(x=posix + 190, y=col2)

            col2 += 40
        else:
            if status[n][0] == 'success':
                success_btn.place(x=posix + 455, y=col3)
            else:
                fail_btn.place(x=posix + 455, y=col3)

            client_name.config(text=clients[n][0])
            client_name.place(x=posix + 370, y=col3)

            col3 += 40
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="switching dialogs">
def switch_dialog(frame_caller):
    frame_caller.destroy()
    save_result()

# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="load home page and run the program">
home_page()
window.mainloop()
#######################################################################################################
