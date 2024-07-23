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
# packages imports
import os
import tkinter as tk
import customtkinter
import gdown
import ttkbootstrap as tkb
import fpdf
from functools import partial
from datetime import date
from tkinter import END
from tkinter import filedialog
from PIL import Image
from CTkPDFViewer import CTkPDFViewer

# project imports
from clients import *
from dialogs.metrics_desc import MetricsDesc
from dialogs.user_guide import UserGuide


#######################################################################################################
# <region desc="retrieving files from google drive">
def load_gDrive_files():
    dest_path = './Patient_Library'
    # sys.argv[0]
    URL = 'https://drive.google.com/drive/folders/1Wa__A5l9zIesIWsTHCXnPX4FSwn-VBuD?usp=share_link'

    if URL.split('/')[-1] == 'usp=share_link':
        URL = URL.replace('usp=share_link', '')

    gdown.download_folder(URL, output=dest_path)
#######################################################################################################


#######################################################################################################
# <region desc="getting all CSV files from a directory/ sub-directory">
def auto_load_csv(auto_load_data):
    path_dir = '/Users/chicobento/Documents/Patient_Library'
    for path, subdir, files in os.walk(path_dir):
        for file in files:
            if file.endswith(".csv") and str.__contains__(file, 'Res'):
                auto_load_data.append(file)


# loading files from selected directory
def load_from_dir_csv(load_from_dir_data, dir_name):
    for path, subdir, files in os.walk(dir_name):
        for file in files:
            if file.endswith(".csv") and str.__contains__(file, 'Res'):
                load_from_dir_data.append(file)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="search client in clients">
def get_unic_cli_result(save_cli, file_name, frame_caller):
    save_cli_result = []

    for cli_idx in range(len(client_list)):
        if client_list[cli_idx].name == save_cli:
            save_cli_result.append(client_list[cli_idx])

    save_results_pdf(save_cli_result, file_name, frame_caller)


# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="search clients selected in clients">
def get_multiple_cli_results(multi_results, file_name, frame_caller):
    save_cli_results = []

    for cli_i in range(len(multi_results)):
        for cli_x in range(len(client_list)):
            if client_list[cli_x].name == multi_results[cli_i]:
                save_cli_results.append(client_list[cli_x])

    save_results_pdf(save_cli_results, file_name, frame_caller)
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
# close
btn_close = customtkinter.CTkImage(light_image=Image.open("image/close.png"),
                                   dark_image=Image.open("image/close.png"), size=(22, 22))
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="setting windows home_page, search_page & result_page">
window = tkb.Window(themename='flatly')
window.title("Tele Sensor")

# set the window
main_x = (window.winfo_screenwidth() // 2) - (750 // 2)
main_y = (window.winfo_screenheight() // 2) - (620 // 3)
window.geometry('{}x{}+{}+{}'.format(750, 620, main_x, main_y))
window.resizable(False, False)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="setting dialog for save_result & autosave">
def set_dialog_window(dialog_frame):
    # set the window
    x = (dialog_frame.winfo_screenwidth() // 2) - (435 // 2)
    y = (dialog_frame.winfo_screenheight() // 2) - (460 // 3)
    dialog_frame.geometry('{}x{}+{}+{}'.format(435, 460, x, y))
    dialog_frame.resizable(False, False)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="setting dialog for success_dialog, fail_dialog & print_dialog">
def feedback_dialog(dialog_frame):
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
# <region desc="switching pages">
def switch_pages(page):
    for frame in main_frame.winfo_children():
        frame.destroy()
        window.update()

    page()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="menu_frame">
menu = tkb.Frame(window, borderwidth=1, style='TLabelframe')
menu.configure(width=750, height=60)

# logo
logo = customtkinter.CTkImage(light_image=Image.open("image/logo.png"),
                              dark_image=Image.open("image/logo.png"), size=(153, 57))
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
                            command=lambda: switch_pages(page=home_page)).place(x=650, y=12)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="masking buttons">
def masking_button():
    customtkinter.CTkButton(menu, text='', width=80, height=42, fg_color="#FFF", state='disabled').place(x=565, y=10)


def masking_buttons():
    # mak button return on processing screen
    customtkinter.CTkButton(menu, text='', width=170, height=42, fg_color="#FFF", state='disabled').place(x=567, y=10)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="home_page_frame">
def home_page():
    home_frame = tkb.Frame(main_frame)

    # search button
    search_btn = customtkinter.CTkImage(light_image=Image.open("image/search.png"),
                                        dark_image=Image.open("image/search.png"), size=(22, 22))
    customtkinter.CTkButton(menu, image=search_btn, text='Search', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: switch_pages(page=search_page)).place(x=650, y=12)

    # method to upload a file
    tkb.Label(home_frame, text="Select file(s)", font=('Roboto', 25)).place(x=135, y=20)

    # tab to select save option
    home_tab = customtkinter.CTkTabview(home_frame, width=670, height=510, corner_radius=6, fg_color='#FAFAFA',
                                        segmented_button_fg_color='#FFF', segmented_button_selected_color='#43A047',
                                        segmented_button_selected_hover_color='#424242',
                                        segmented_button_unselected_color='#212121',
                                        segmented_button_unselected_hover_color='#757575')
    home_tab.place(x=40, y=15)

    # ###########################################################################################################
    # ############################################## LOAD FILES ON LOAD #########################################
    files_tab = home_tab.add(" SELECT FILE(S) ")

    tkb.Label(files_tab, text="File accepted .CSV", foreground='#424242', font=('Roboto', 12)).place(x=120, y=267)

    # button to select all items once
    cbx_state = tk.IntVar()

    def select_all():
        if cbx_state.get():
            loaded_files.select_set(0, END)
        else:
            loaded_files.select_clear(0, END)

    cbx_state = customtkinter.CTkCheckBox(files_tab, text="Select All", font=('Roboto', 12), hover_color="#424242",
                                          fg_color='#4CAF50', text_color="#212121", variable=cbx_state,
                                          command=select_all)
    cbx_state.place(x=450, y=267)

    # get values selected
    def selected_items():
        selected_loaded_files = []
        selected_idx = loaded_files.curselection()

        for index in selected_idx:
            selected_loaded_files.append(loaded_files.get(index))
        return selected_loaded_files

    # getting all CSV files from directory and subdirectories
    # NOTE: the code still loading files from local directory 'Patient_Library'
    csv_file_list = []
    auto_load_csv(csv_file_list)

    # list all CSV files into listbox
    loaded_files = tk.Listbox(files_tab, selectmode="multiple", width=50, height=12, font=('Arial', 13), border=4,
                              selectborderwidth=2)
    loaded_files.place(x=120, y=15)

    # listing all files into the listbox
    for file_idx in range(len(csv_file_list)):
        loaded_files.insert(END, csv_file_list[file_idx])
        loaded_files.itemconfigure(file_idx, selectbackground='#4CAF50')

    customtkinter.CTkButton(files_tab, text="Click to learn more", text_color='#03A9F4', hover_color='#FAFAFA',
                            fg_color='#FAFAFA', command=MetricsDesc).place(x=240, y=335)

    customtkinter.CTkCheckBox(master=files_tab, text="Process by metrics", width=25, height=25, font=("Roboto", 22),
                              fg_color="#4CAF50", hover_color="#424242", text_color="#212121").place(x=220, y=310)

    customtkinter.CTkButton(files_tab, text='PROCESS', width=170, height=48, fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: processing_page(selected_items(), home_frame)).place(x=235, y=400)

    # ###########################################################################################################
    # ########################################## LOAD FILES FROM DIRECTORY ######################################
    opendir_tab = home_tab.add(" SEARCH FILE(S) ")

    def open_directory():
        folder = tk.filedialog.askdirectory(title='Select file...', initialdir='Documents')
        csv_files_from_dir = []
        load_from_dir_csv(csv_files_from_dir, folder)

        if len(csv_files_from_dir) > 0:
            # get values selected
            def select_items_dir():
                selected_opened_files = []
                selected_idx = selected_files_dir.curselection()

                for index in selected_idx:
                    selected_opened_files.append(selected_files_dir.get(index))
                return selected_opened_files

            # list all CSV files into listbox
            selected_files_dir = tk.Listbox(opendir_tab, selectmode="multiple", width=50, height=12, font=('Arial', 13),
                                            border=4, selectborderwidth=2)
            selected_files_dir.place(x=120, y=100)

            # listing all files into the listbox
            for f_idx in range(len(csv_files_from_dir)):
                selected_files_dir.insert(END, csv_files_from_dir[f_idx])
                selected_files_dir.itemconfigure(f_idx, selectbackground='#4CAF50')

            customtkinter.CTkButton(opendir_tab, text='PROCESS', width=170, height=48, fg_color="#1976D2",
                                    hover_color="#424242", font=('Roboto', 18),
                                    command=lambda: processing_page(select_items_dir(), home_frame)).place(x=235, y=400)
        else:
            tkb.Label(opendir_tab, text='Folder not selected or contains invalid files! \n Try again.',
                      foreground='#E53935', font=('Arial', 16, 'bold'), justify='center').place(x=155, y=220)

    # upload button
    customtkinter.CTkButton(opendir_tab, image=upload_btn, text='SELECT DIR', width=50, height=40, compound="left",
                            fg_color="#424242", hover_color="#90A4AE", corner_radius=24,
                            command=lambda: open_directory()).place(x=255, y=20)
    tkb.Label(opendir_tab, text="File accepted .pdf", font=('Roboto', 13)).place(x=275, y=65)

    # button for help
    customtkinter.CTkButton(home_frame, image=helper, text='', width=29, height=32, compound="left", fg_color="#FFFFFF",
                            hover_color="#424242", corner_radius=5, command=UserGuide).place(x=705, y=520)

    home_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="processing_page_frame">
def processing_page(files_chosen, caller_frame):
    processing_frame = tkb.Frame(main_frame)
    masking_buttons()
    caller_frame.destroy()

    tkb.Label(processing_frame, text="Processing...", font=('Roboto', 25)).place(x=310, y=4)

    # adding image icon
    heart_rate = customtkinter.CTkImage(light_image=Image.open("image/heart_rate.gif"),
                                        dark_image=Image.open("image/heart_rate.gif"), size=(635, 330))
    customtkinter.CTkLabel(processing_frame, text="", image=heart_rate).place(x=50, y=50)

    # adding legend to heart rate waves CGI & HR
    hr = customtkinter.CTkImage(light_image=Image.open("image/hr.png"), dark_image=Image.open("image/hr.png"),
                                size=(22, 22))
    customtkinter.CTkButton(processing_frame, image=hr, text='', width=18, height=20, compound="left",
                            fg_color="#000000", state='disabled', corner_radius=5).place(x=510, y=383)
    tkb.Label(processing_frame, text="HR", style="dark").place(x=550, y=387)

    cgi = customtkinter.CTkImage(light_image=Image.open("image/cgi.png"), dark_image=Image.open("image/cgi.png"),
                                 size=(22, 22))
    customtkinter.CTkButton(processing_frame, image=cgi, text='', width=18, height=20, compound="left",
                            fg_color="#000000", state='disabled', corner_radius=5).place(x=610, y=383)
    tkb.Label(processing_frame, text="CGI", style="dark").place(x=650, y=387)

    # button for help
    customtkinter.CTkButton(processing_frame, text='STOP', width=170, height=48, fg_color="#EF5350",
                            hover_color="#424242", font=('Roboto', 18, 'bold'), corner_radius=5,
                            command=lambda: results_page(client_list, 'Simone Cole',
                                                         processing_frame)).place(x=275, y=445)

    tkb.Label(processing_frame, style='success', text=files_chosen, font=('Verdana', 13),
              wraplength=780).place(x=5, y=495)

    processing_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="search_page_frame">
def search_page():
    search_frame = tkb.Frame(main_frame)
    masking_button()
    return_page()

    tkb.Label(search_frame, text="Review Metric Results", font=('Roboto', 25)).place(x=265, y=17)
    lb_file_opened = tkb.Label(search_frame)

    # method to upload file
    def open_directory():
        file = tk.filedialog.askopenfilename(title='Select file...', initialdir="TeleSensor_Results",
                                             filetypes=[("PDF file", "*.pdf")])

        if file and str.__contains__(file, 'TeleSensor_Results'):
            lb_file_opened.configure(text=str.split((format(file)), 'TeleSensor/')[1], foreground='#212121',
                                     font=('Roboto', 13))
            lb_file_opened.place(x=220, y=145)

            customtkinter.CTkButton(search_frame, image=eye, text='View PDF', width=50, height=40, fg_color="#F4511E",
                                    hover_color="#CFD8DC", text_color="#212121", font=('Roboto', 18),
                                    command=lambda: read_pdf(lb_file_opened.cget('text'))).place(x=315, y=190)
        else:
            lb_file_opened.configure(text='File not selected or not valid! \n Try again.', foreground='#E53935',
                                     font=('Arial', 16, 'bold'), justify='center')
            lb_file_opened.place(x=255, y=155)

    # upload button
    customtkinter.CTkButton(search_frame, image=upload_btn, text='SELECT FILE', width=50, height=40, compound="left",
                            fg_color="#424242", hover_color="#90A4AE", corner_radius=24,
                            command=lambda: open_directory()).place(x=295, y=70)

    tkb.Label(search_frame, text="File accepted .pdf", font=('Roboto', 13)).place(x=315, y=115)

    # recent results panel
    recent_tab = customtkinter.CTkTabview(search_frame, width=620, height=230, corner_radius=12, fg_color="#EEEEEE")
    recent_tab.place(x=65, y=235)

    # list last 9 recent results
    tkb.Label(search_frame, text="Recent Metrics", foreground="#01579B", background="#EEEEEE",
              font=('Roboto', 23)).place(x=290, y=265)

    # calling function to design the table
    recent_result_table(search_frame)

    # adding legend to buttons success & fail
    customtkinter.CTkButton(search_frame, image=eye, text='', width=20, height=22, compound="left", fg_color="#81C784",
                            state='disabled', corner_radius=5).place(x=75, y=472)
    tkb.Label(search_frame, text="Succeed", style="dark").place(x=110, y=474)

    customtkinter.CTkButton(search_frame, image=eye, text='', width=30, height=22, compound="left", fg_color="#E57373",
                            state='disabled', corner_radius=5).place(x=197, y=472)
    tkb.Label(search_frame, text="Failed", style="dark").place(x=232, y=474)

    # button for help
    customtkinter.CTkButton(main_frame, image=helper, text='', width=29, height=32, compound="left", fg_color="#FFFFFF",
                            hover_color="#424242", corner_radius=5, command=UserGuide).place(x=705, y=520)

    search_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="result_page_frame">
def results_page(cli_list, cli_opened, caller_frame):
    result_frame = tkb.Frame(main_frame)
    return_page()
    caller_frame.destroy()

    # return to list button
    list_result = customtkinter.CTkImage(light_image=Image.open("image/result_list.png"),
                                         dark_image=Image.open("image/result_list.png"), size=(20, 20))
    customtkinter.CTkButton(menu, image=list_result, text='Results', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: switch_pages(page=search_page)).place(x=650, y=12)

    # function to list clients into the slider
    def list_result(value):
        lbl_result.configure(text=value + "'s Result")

        for client in cli_list:
            if client.name == value:
                if client.result_status:
                    lbl_result.configure(fg_color='#4CAF50')
                else:
                    lbl_result.configure(fg_color='#E53935')

                lb_res_date.configure(text=client.name)
                lb_hr.configure(text=client.heart_rate)
                lb_rms_val.configure(text=client.rms_value)
                lb_rms_acc.configure(text=f"{client.rms_accuracy} %")
                lb_rms_err.configure(text=f"{client.rms_error} %")
                hr_graph.configure(light_image=Image.open("TeleSensor_Results/hr_graphs/" + client.hr_graph),
                                   dark_image=Image.open("TeleSensor_Results/hr_graphs/" + client.hr_graph),
                                   size=(325, 285))

    # getting all client names
    cli_names = []
    for cli in cli_list:
        cli_names.append(cli.name)

    customtkinter.CTkSegmentedButton(result_frame, values=cli_names, font=('Roboto', 15), height=30, fg_color='#616161',
                                     selected_color='#4CAF50', unselected_hover_color='#212121', corner_radius=0,
                                     selected_hover_color='#212121', unselected_color='#616161',
                                     command=list_result).place(x=0, y=3)

    # recent results panel
    recent_tab = customtkinter.CTkTabview(result_frame, width=600, height=165, corner_radius=12, fg_color="#EEEEEE",
                                          border_color='red')
    recent_tab.place(x=65, y=55)

    # find the client passed as parameter to see results
    cli_passed = ''
    for cli_found in range(len(cli_list)):
        if cli_list[cli_found].name in cli_opened:
            cli_passed = cli_list[cli_found]

    lbl_result = customtkinter.CTkButton(result_frame, text=f"{cli_passed.name}'s Result", width=160, height=35,
                                         font=('Roboto', 18, 'bold'), state='disable')
    if cli_passed.result_status:
        lbl_result.configure(fg_color='#4CAF50')
    else:
        lbl_result.configure(fg_color='#E53935')
    lbl_result.place(x=270, y=60)

    # save result button
    save_btn = customtkinter.CTkImage(light_image=Image.open("image/save.png"),
                                      dark_image=Image.open("image/save.png"),
                                      size=(22, 22))
    customtkinter.CTkButton(menu, image=save_btn, text='Save ', width=37, height=36, compound="left",
                            fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                            command=lambda: save_options(cli_list, cli_opened)).place(x=565, y=12)
    # adding labels from result
    tkb.Label(result_frame, text="Date: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=105, y=112)
    lb_res_date = tkb.Label(result_frame, text=cli_passed.result_date, foreground="#388E3C", background="#EEEEEE",
                            font=('Roboto', 16))
    lb_res_date.place(x=145, y=112)

    tkb.Label(result_frame, text="Heart Rate: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=300, y=112)
    lb_hr = tkb.Label(result_frame, text=cli_passed.heart_rate, foreground="#388E3C", background="#EEEEEE",
                      font=('Roboto', 16))
    lb_hr.place(x=380, y=112)

    tkb.Label(result_frame, text="Metric: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=495, y=112)
    tkb.Label(result_frame, text="Bpm", foreground="#388E3C", background="#EEEEEE",
              font=('Roboto', 16)).place(x=547, y=112)

    tkb.Label(result_frame, text="RMS Value: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=105, y=165)
    lb_rms_val = tkb.Label(result_frame, text=cli_passed.rms_value, foreground="#388E3C", background="#EEEEEE",
                           font=('Roboto', 16))
    lb_rms_val.place(x=190, y=165)

    tkb.Label(result_frame, text="RMS Accuracy: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=300, y=165)
    lb_rms_acc = tkb.Label(result_frame, text=f" {cli_passed.rms_accuracy} %", foreground="#388E3C",
                           background="#EEEEEE", font=('Roboto', 16))
    lb_rms_acc.place(x=405, y=165)

    tkb.Label(result_frame, text="RMS Error: ", foreground="#616161", background="#EEEEEE",
              font=('Roboto', 15)).place(x=495, y=165)
    lb_rms_err = tkb.Label(result_frame, text=f" {cli_passed.rms_error} %", foreground="#388E3C",
                           background="#EEEEEE", font=('Roboto', 16))
    lb_rms_err.place(x=570, y=165)

    # heart rate graph result
    hr_graph = customtkinter.CTkImage(light_image=Image.open("TeleSensor_Results/hr_graphs/" + cli_passed.hr_graph),
                                      dark_image=Image.open("TeleSensor_Results/hr_graphs/" + cli_passed.hr_graph),
                                      size=(325, 285))
    customtkinter.CTkLabel(result_frame, text="", image=hr_graph).place(x=240, y=235)

    result_frame.pack(fill=tkb.BOTH, expand=True)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="save_result">
def save_options(cli_list, client_parm):
    tkb.Frame(main_frame)
    save_frame = tkb.Toplevel()
    save_frame.title("Save Result")
    set_dialog_window(save_frame)

    # tab to select save option
    save_tab = customtkinter.CTkTabview(save_frame, width=394, height=400, corner_radius=12, fg_color='#E0E0E0',
                                        segmented_button_fg_color='#FFF', segmented_button_selected_color='#66BB6A',
                                        segmented_button_selected_hover_color='#424242',
                                        segmented_button_unselected_color='#424242',
                                        segmented_button_unselected_hover_color='#757575')
    save_tab.place(x=20, y=38)
    # adding image icon
    PDF = customtkinter.CTkImage(light_image=Image.open("image/PDF.png"),
                                 dark_image=Image.open("image/PDF.png"), size=(33, 33))
    customtkinter.CTkLabel(save_frame, text="", image=PDF).place(x=5, y=10)
    tkb.Label(save_frame, text="Save File", font=('Roboto', 20, 'bold')).place(x=45, y=12)

    # button cancel
    customtkinter.CTkButton(save_frame, image=btn_close, text='', width=25, height=34, compound="left",
                            fg_color="#EF5350", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: save_frame.destroy()).place(x=390, y=8)

    # ############################################### SAVE ACTUAL CLIENT #######################################
    actual_tab = save_tab.add("ACTUAL")
    tkb.Label(actual_tab, text='File Name:', font=('Roboto', 16), background='#E0E0E0').place(x=40, y=22)
    actual_f_name = customtkinter.CTkEntry(actual_tab, width=290, height=40, font=('Roboto', 13), fg_color='#FFF',
                                           border_width=1, border_color='#BDBDBD', text_color='#000',
                                           placeholder_text='Result file name')
    actual_f_name.insert(END, str(client_parm + date.today().strftime("_%m_%d_%Y")))
    actual_f_name.place(x=40, y=47)

    actual_info = customtkinter.CTkTabview(actual_tab, width=330, height=120, corner_radius=12, fg_color="#FFE082")
    actual_info.place(x=15, y=101)
    tkb.Label(actual_tab, text='The PDF file will be saved into documents inside "TeleSensor_Results" folder. \n'
                               'To edit file name click on the name above.', justify='center', wraplength=300,
              font=('Roboto', 13, 'bold'), background='#FFE082').place(x=45, y=134)

    # button save
    customtkinter.CTkButton(actual_tab, text='SAVE', width=170, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: get_unic_cli_result(client_parm, actual_f_name.get(),
                                                                save_frame)).place(x=90, y=260)

    # ############################################### SAVE MULTIPLE CLIENTS ##################################
    multiple_tab = save_tab.add("MULTIPLES")
    
    tkb.Label(multiple_tab, text='File Name:', font=('Roboto', 15), background='#E0E0E0').place(x=40, y=-6)
    multi_f_name = customtkinter.CTkEntry(multiple_tab, width=250, height=35, font=('Roboto', 13), fg_color='#FFF',
                                          border_width=1, border_color='#BDBDBD', text_color='#000',
                                          placeholder_text='Result file name')
    multi_f_name.insert(END, str("Multi_Cli_Selected" + date.today().strftime("_%m_%d_%Y")))
    multi_f_name.place(x=46, y=15)

    tkb.Label(multiple_tab, text='Select the clients', font=('Roboto', 12), background='#E0E0E0').place(x=120, y=270)

    # get values selected
    def selected_results():
        client_results = []
        selected_idx = list_cli_results.curselection()

        for index in selected_idx:
            client_results.append(list_cli_results.get(index))
        return client_results

    # list all results into listbox to be selected
    list_cli_results = tk.Listbox(multiple_tab, selectmode="multiple", width=30, font=('Arial', 13),
                                  border=4, selectborderwidth=2)
    list_cli_results.place(x=45, y=60)

    # populating all clients result into listbox
    for cli_idx in range(len(cli_list)):
        list_cli_results.insert(END, '{: >5}'.format(cli_list[cli_idx].name))
        if cli_list[cli_idx].result_status == 1:
            list_cli_results.itemconfigure(cli_idx, foreground='#388E3C')
        else:
            list_cli_results.itemconfigure(cli_idx, foreground='#E53935')

        list_cli_results.itemconfigure(cli_idx, selectbackground='#4CAF50')

    # button save
    customtkinter.CTkButton(multiple_tab, text='SAVE CLIENTS', width=170, height=40, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: get_multiple_cli_results(selected_results(), multi_f_name.get(),
                                                                     save_frame)).place(x=85, y=298)

    # ############################################### SAVE ALL CLIENTS ##################################
    all_tab = save_tab.add(" ALL ")

    tkb.Label(all_tab, text='File Name:', font=('Roboto', 16), background='#E0E0E0').place(x=68, y=5)
    all_f_name = customtkinter.CTkEntry(all_tab, width=245, height=40, font=('Roboto', 13), fg_color='#FFF',
                                        border_width=1, border_color='#BDBDBD', text_color='#000',
                                        placeholder_text='Result file name')
    all_f_name.insert(END, str("All_Cli_Results" + date.today().strftime("_%m_%d_%Y")))
    all_f_name.place(x=65, y=25)

    all_info = customtkinter.CTkTabview(all_tab, width=322, height=160, corner_radius=12, fg_color="#FFE082")
    all_info.place(x=22, y=66)
    tkb.Label(all_tab, text=' The file will include results from all clients processed. \n '
                            'It will be saved into documents inside "TeleSensor_Results" folder.', justify='center',
              wraplength=300, font=('Roboto', 13, 'bold'), background='#FFE082').place(x=40, y=110)

    # button save
    customtkinter.CTkButton(all_tab, text='SAVE ALL', width=170, height=48, compound="left", fg_color="#1976D2",
                            hover_color="#424242", font=('Roboto', 18),
                            command=lambda: save_results_pdf(cli_list, all_f_name.get(), save_frame)).place(x=90, y=260)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="display PDF result">
def read_pdf(file_name):
    tkb.Frame(main_frame)
    pdf_frame = tkb.Toplevel()
    pdf_frame.title("TeleSensor PDF Result")

    # set the window
    x = (pdf_frame.winfo_screenwidth() // 2) - (745 // 2)
    y = (pdf_frame.winfo_screenheight() // 2) - (760 // 3)
    pdf_frame.geometry('{}x{}+{}+{}'.format(745, 760, x, y))
    pdf_frame.resizable(False, False)

    # print
    btn_print = customtkinter.CTkImage(light_image=Image.open("image/printer.png"),
                                       dark_image=Image.open("image/printer.png"), size=(22, 22))
    customtkinter.CTkButton(pdf_frame, image=btn_print, text='Print ', width=37, height=36, fg_color="#1976D2",
                            hover_color="#424242", corner_radius=5,
                            command=lambda: print_file(file_name)).place(x=480, y=8)

    # return to list button
    btn_res = customtkinter.CTkImage(light_image=Image.open("image/return.png"),
                                     dark_image=Image.open("image/return.png"), size=(20, 20))
    customtkinter.CTkButton(pdf_frame, image=btn_res, text='Return', width=37, height=36, fg_color="#1976D2",
                            hover_color="#424242", corner_radius=5,
                            command=lambda: pdf_frame.destroy()).place(x=565, y=8)

    customtkinter.CTkButton(pdf_frame, image=btn_close, text='Close', width=37, height=36, fg_color="#F44336",
                            hover_color="#424242", corner_radius=5,
                            command=lambda: pdf_frame.destroy()).place(x=660, y=8)

    # check if the file path is complete
    pattern_file = "TeleSensor_Results/TeleSensor_Result.pdf"

    if str.split(file_name, '/')[0] == 'TeleSensor_Results':
        CTkPDFViewer(pdf_frame, file=file_name, width=710, height=680).place(x=5, y=50)
    else:
        # check if the client result has file name
        for cli_x in range(len(client_list)):
            if client_list[cli_x].name == file_name:
                if len(client_list[cli_x].file_name) > 4:
                    file_n = f"TeleSensor_Results/{client_list[cli_x].file_name}"
                    if os.path.isfile(file_n):
                        CTkPDFViewer(pdf_frame, file=file_n, width=710, height=680).place(x=5, y=50)
                        print('File found')
                    else:
                        CTkPDFViewer(pdf_frame, file=pattern_file, width=710, height=680).place(x=5, y=50)
                        print('File not found')
                else:
                    CTkPDFViewer(pdf_frame, file=pattern_file, width=710, height=680).place(x=5, y=50)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="save_result to PDF">
def save_results_pdf(client_results, file_name, frame_caller):
    # save at directory
    save_dir = "TeleSensor_Results/"
    cur_date = date.today().strftime("%B %d, %Y")

    # create a new obj PDF and new page
    pdf = fpdf.FPDF()

    # populate client variables with results
    for cli_idx in range(len(client_results)):
        pdf.add_page()

        # setting styles
        pdf.set_font('Arial', 'B', 16)
        pdf.set_text_color(0, 68, 148)
        pdf.cell(0, 15, txt='TeleSensor Heart Rate Result', align='C', border=1)
        pdf.multi_cell(0, 25, txt='', align='C')

        pdf.set_font('Arial', 'BU', 14)
        pdf.set_text_color(19, 99, 9)
        pdf.cell(75, 17, txt=client_results[cli_idx].name, align='R')

        if client_results[cli_idx].result_status == 1:
            pdf.cell(75, 17, txt="Status: Pass", align='R')
        else:
            pdf.set_text_color(225, 45, 45)
            pdf.cell(75, 17, txt="Status: Fail", align='R')
        pdf.multi_cell(0, 20, txt='', align='C')

        pdf.set_font('Arial', '', 12)
        pdf.set_text_color(51, 51, 51)
        pdf.cell(65, 20, txt=f"Date: {cur_date}", align='L')
        pdf.cell(60, 20, txt=f"Heart Rate: {client_results[cli_idx].heart_rate}", align='C')
        pdf.cell(60, 20, txt='Metric: Bpm', align='R', border=0)
        pdf.multi_cell(0, 20, txt='', align='C')

        pdf.cell(65, 20, txt=f"RMS Value: {client_results[cli_idx].rms_value}", align='L')
        pdf.cell(60, 20, txt=f"RMS Accuracy: {client_results[cli_idx].rms_accuracy} %", align='C')
        pdf.cell(60, 20, txt=f"RMS Error: {client_results[cli_idx].rms_error} %", align='R')
        pdf.multi_cell(0, 20, txt='', align='C')

        pdf.set_font('Arial', 'BU', 16)
        pdf.set_text_color(19, 99, 9)
        pdf.cell(0, 30, txt='Graph Metric', align='C')
        pdf.image('TeleSensor_Results/hr_graphs/Brian Scott_graph.png', 50, 120, 95, 75)

    # path and file name
    if not os.path.exists(save_dir):
        fail_dialog(frame_caller)
    else:
        file_path = save_dir + file_name + '.pdf'
        pdf.output(file_path, 'F')

        success_dialog(frame_caller, file_path)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="success dialog">
def success_dialog(frame_caller, cli_saved):
    tkb.Frame(main_frame)

    success_frame = tkb.Toplevel()
    success_frame.title("Saved Successfully")
    feedback_dialog(success_frame)

    # adding image icon
    success_icon = customtkinter.CTkImage(light_image=Image.open("image/success.png"),
                                          dark_image=Image.open("image/success.png"), size=(70, 70))
    customtkinter.CTkLabel(success_frame, text="", image=success_icon).place(x=180, y=15)

    feedback = str.split(cli_saved, 'TeleSensor_Results/')
    tkb.Label(success_frame, text=feedback[1], justify='center').place(x=100, y=100)

    # message label
    tkb.Label(success_frame, text='File saved successfully!', justify='center',
              font=('Roboto', 17, 'bold'), foreground='#212121').place(x=120, y=150)

    # button save
    customtkinter.CTkButton(success_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: success_frame.destroy()).place(x=165, y=200)
    frame_caller.destroy()
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="fail dialog">
def warn_dialog(message):
    warn_frame = tkb.Frame(main_frame)

    warn_frame = tkb.Toplevel()
    warn_frame.title("Warning")
    feedback_dialog(warn_frame)

    # adding image icon
    warn_icon = customtkinter.CTkImage(light_image=Image.open("image/warning.png"),
                                       dark_image=Image.open("image/warning.png"), size=(80, 80))
    customtkinter.CTkLabel(warn_frame, text="", image=warn_icon).place(x=170, y=20)

    tkb.Label(warn_frame, text='Something went wrong! Try again', justify='center',
              font=('Roboto', 17, 'bold'), foreground='#212121').place(x=85, y=115)

    # message label
    tkb.Label(warn_frame, text=message, justify='center', font=('Roboto', 14), foreground='#212121').place(x=140, y=145)

    # button save
    customtkinter.CTkButton(warn_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: warn_frame.destroy()).place(x=165, y=190)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="fail dialog">
def fail_dialog(frame_caller):
    fail_frame = tkb.Frame(main_frame)

    fail_frame = tkb.Toplevel()
    fail_frame.title("Failed to Save")
    feedback_dialog(fail_frame)

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
def print_dialog(file_printing):
    print_frame = tkb.Frame(main_frame)

    print_frame = tkb.Toplevel()
    print_frame.title("Printing File")
    feedback_dialog(print_frame)

    # adding image icon
    success_icon = customtkinter.CTkImage(light_image=Image.open("image/printing.png"),
                                          dark_image=Image.open("image/printing.png"), size=(85, 85))
    customtkinter.CTkLabel(print_frame, text="", image=success_icon).place(x=170, y=20)

    # printing progress
    file = str.split(str.split(file_printing, '/')[1], '_')[0]
    tkb.Label(print_frame, text=f"Printing {file}'s result", justify='center',
              font=('Roboto', 20), foreground='#212121').place(x=80, y=120)

    # button to close popup
    customtkinter.CTkButton(print_frame, text='OK', width=100, height=48, compound="left",
                            fg_color="#1976D2", hover_color="#424242", font=('Roboto', 18),
                            command=lambda: print_frame.destroy()).place(x=165, y=190)
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="recent_results table">
def recent_result_table(search_frame):
    posix = 123
    col1 = 323
    col2 = 323
    col3 = 323
    n = 0

    for client in client_list:
        # success button
        success_btn = customtkinter.CTkButton(search_frame, image=eye, text='', width=20, height=22, compound="left",
                                              fg_color="#81C784", hover_color="#90A4AE", corner_radius=5)
        # fail button
        fail_btn = customtkinter.CTkButton(search_frame, image=eye, text='', width=30, height=22, compound="left",
                                           fg_color="#E57373", hover_color="#90A4AE", corner_radius=5)
        client_name = tkb.Label(search_frame, foreground='#01579B', background="#EEEEEE", font=('Roboto', 14))

        if n <= 2:
            if client.result_status:
                success_btn.configure(command=partial(read_pdf, client.name))
                success_btn.place(x=posix + 107, y=col1)
            else:
                fail_btn.configure(command=partial(read_pdf, client.name))
                fail_btn.place(x=posix + 107, y=col1)

            client_name.configure(text=client.name)
            client_name.place(x=posix, y=col1)

            col1 += 40
        elif n <= 5:
            if client.result_status:
                success_btn.configure(command=partial(read_pdf, client.name))
                success_btn.place(x=posix + 285, y=col2)
            else:
                fail_btn.configure(command=partial(read_pdf, client.name))
                fail_btn.place(x=posix + 285, y=col2)

            client_name.config(text=client.name)
            client_name.place(x=posix + 190, y=col2)

            col2 += 40
        else:
            if client.result_status:
                success_btn.configure(command=partial(read_pdf, client.name))
                success_btn.place(x=posix + 455, y=col3)
            else:
                fail_btn.configure(command=partial(read_pdf, client.name))
                fail_btn.place(x=posix + 455, y=col3)

            client_name.config(text=client.name)
            client_name.place(x=posix + 370, y=col3)

            col3 += 40
        n += 1
# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="print PDF file">
def print_file(file_to_print):
    print('Printing file: {}'.format(file_to_print))

# <endregion>
#######################################################################################################


#######################################################################################################
# <region desc="load files from Google Drive, home page and run the program">
home_page()
# load_gDrive_files()
window.mainloop()
#######################################################################################################
