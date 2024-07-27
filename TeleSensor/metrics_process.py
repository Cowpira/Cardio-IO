from tkinter import *
import customtkinter
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from PIL import Image
import os
from self import self
import main
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def calculate_metrics(df):
    metrics = {'difference': df['HR'] - df['SpO2HR'], 'convergence_time': (df['HR'] - df['SpO2HR']).abs().idxmin(),
               'batch_average': df[['HR', 'SpO2HR']].mean()}
    return metrics


def export_to_pdf(csv_path):
    save_dir = "TeleSensor_Results/PDF_Reports/"
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    file_name = csv_path.split('/')[-1].split('.')[0]

    selected_files = [csv_path]
    data = [pd.read_csv(csv_path)]

    for file, df in zip(selected_files, data):
        metrics = calculate_metrics(df)
        fig = plot_metrics(df, metrics, os.path.basename(file))
        img_path = f"{os.path.splitext(file)[0]}.png"
        fig.savefig(img_path)
        plt.close(fig)

        pdf.add_page()
        pdf.image(img_path, x=10, y=10, w=170)
        os.remove(img_path)

    # path and file name
    if not os.path.exists(save_dir):
        main.fail_dialog(Frame)
    else:
        file_path = save_dir + file_name + '.pdf'
        pdf.output(file_path, 'F')
        main.success_dialog(file_name)


def plot_metrics(df, metrics, file_name):
    fig, axs = plt.subplots(3, figsize=(6.1, 9.6))
    fig.suptitle(f"Metrics for {file_name}", fontsize=12, fontfamily='Sans Serif', color='#212121')

    # Difference between HR and SpO2HR
    axs[0].plot(df['time(s)'], metrics['difference'], color='#FF0000')
    axs[0].set_title(f" Difference between HR and SpO2HR:          Means{metrics['difference'].mean():.2f}",
                     fontsize=11, color='#2962FF', pad=10)
    # graphing plot
    axs[0].set_xlabel('Time (s)', fontsize=9)
    axs[0].set_ylabel('Difference', fontsize=9)

    # HR and SpO2HR Over Time
    axs[1].plot(df['time(s)'], df['HR'], label='HR', color='#000000')
    axs[1].plot(df['time(s)'], df['SpO2HR'], label='SpO2HR', color='#FF0000')

    axs[1].set_title(f"HR and SpO2HR Over Time         Convergence Time {metrics['convergence_time']}s",
                     fontsize=10, color='#2962FF')
    # graphing plot
    axs[1].set_xlabel('Time (s)', fontsize=9)
    axs[1].set_ylabel('Heart Rate', fontsize=9)

    # Batch Averages
    axs[2].bar(['Batch Average HR', 'Batch Average SpO2HR'], metrics['batch_average'], color=['#000000', '#FF0000'])
    axs[2].set_title(f"Batch Averages     Avg. HR: {metrics['batch_average']['HR']:.2f} "
                     f"      Avg. SpO2HR: {metrics['batch_average']['SpO2HR']:.2f}", fontsize=10, color='#2962FF')

    plt.tight_layout(rect=[0.0, 0.03, 1.0, 0.95])
    plt.subplots_adjust(hspace=0.4)
    return fig


def show_plots(file_path):
    # Only create one plot window
    if hasattr(self, 'plot_frame') and self.plot_frame.winfo_exists():
        self.plot_frame.lift()
    else:
        self.plot_frame = Toplevel()
        self.plot_frame.title("TeleSensor Graph Plot")

        # defining and loading local variables
        self.selected_files = [file_path]
        self.data = [pd.read_csv(file_path)]

        btn_save = customtkinter.CTkFrame(self.plot_frame, width=70, height=30, fg_color='#FFF')
        btn_save.grid(row=0, column=0, sticky=customtkinter.N+customtkinter.E+customtkinter.W)
        # btn to save plot as PDF
        icon_save = customtkinter.CTkImage(light_image=Image.open("image/save.png"),
                                           dark_image=Image.open("image/save.png"), size=(18, 18))
        customtkinter.CTkButton(btn_save, image=icon_save, text="Save", width=40, height=36,
                                fg_color="#1976D2", hover_color="#424242", corner_radius=5,
                                command=lambda: export_to_pdf(file_path)).pack(side='left', padx=4, pady=7)

        # set the window
        x = (self.plot_frame.winfo_screenwidth() // 2) - (750 // 2)
        y = (self.plot_frame.winfo_screenheight() // 2) - (930 // 3)
        self.plot_frame.geometry('{}x{}+{}+{}'.format(750, 930, x, y))
        self.plot_frame.resizable(False, True)

        btn_previous = customtkinter.CTkFrame(self.plot_frame, fg_color='#FFF')
        btn_previous.grid(row=0, column=0)

        btn_next = customtkinter.CTkFrame(self.plot_frame, fg_color='#FFF')
        btn_next.grid(row=0, column=2)

        self.plot_frame = Frame(self.plot_frame, width=745, height=930)
        self.plot_frame.grid(row=0, column=1)

        current_index = [0]

        def update_plot(index):
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            fig = plot_metrics(self.data[index], calculate_metrics(self.data[index]),
                               os.path.basename(self.selected_files[index]))
            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        def next_plot():
            if current_index[0] < len(self.selected_files) - 1:
                current_index[0] += 1
                update_plot(current_index[0])

        def previous_plot():
            if current_index[0] > 0:
                current_index[0] -= 1
                update_plot(current_index[0])

        # Only show buttons if more than one file is uploaded
        if len(self.selected_files) >= 1:
            # previous plot
            icon_prev = customtkinter.CTkImage(light_image=Image.open("image/previous.png"),
                                               dark_image=Image.open("image/previous.png"), size=(22, 22))
            customtkinter.CTkButton(btn_previous, image=icon_prev, text='', width=40, height=36, fg_color="#1976D2",
                                    hover_color="#424242", corner_radius=5, command=previous_plot).pack()

            # next plot
            icon_next = customtkinter.CTkImage(light_image=Image.open("image/next.png"),
                                               dark_image=Image.open("image/next.png"), size=(20, 20))
            customtkinter.CTkButton(btn_next, image=icon_next, text='', width=40, height=36, fg_color="#1976D2",
                                    hover_color="#424242", corner_radius=5, command=next_plot).pack()

        update_plot(current_index[0])
