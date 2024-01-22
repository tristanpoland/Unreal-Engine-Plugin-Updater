
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, filedialog
from PIL import Image
import subprocess
import sys
import os

class UEPluginConv:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\fortb\OneDrive\Documents\New Python\Unreal Plugin Convertor\Online\build\assets\frame0")


        self.window = Tk()

        self.window.geometry("375x350")
        self.window.configure(bg = "#FFFFFF")
        self.window.title = "Unreal Plugin Convertor"
        

        self.plugin_path = tk.StringVar('')
        self.source_version = tk.StringVar('')
        self.target_version_runbat_file = tk.StringVar('')
        self.output_folder_path = tk.StringVar('')


        canvas = Canvas(
            self.window,
            bg = "#f16865",
            height = 350,
            width = 375,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            188.0,
            175.0,
            image=image_image_1
        )

        entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            187.5,
            175.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#f16865",
            fg="#ffffff",
            highlightthickness=0,
            textvariable=self.plugin_path
            
        )
        entry_1.place(
            x=100.0,
            y=168.0,
            width=175.0,
            height=12.0
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            187.5,
            114.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#f16865",
            fg="#ffffff",
            highlightthickness=0,
            textvariable=self.target_version_runbat_file
        )
        entry_2.place(
            x=100.0,
            y=107.0,
            width=175.0,
            height=12.0
        )

        entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            187.5,
            239.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#f16865",
            fg="#ffffff",
            highlightthickness=0,
            textvariable=self.output_folder_path
        )
        entry_3.place(
            x=100.0,
            y=232.0,
            width=175.0,
            height=12.0
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        batch_button = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_bat_file,
            relief="flat"
        )
        batch_button.place(
            x=301.0,
            y=100.0,
            width=26.0,
            height=25.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        plugin_button = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_plugin,
            relief="flat"
        )
        plugin_button.place(
            x=301.0,
            y=163.0,
            width=26.0,
            height=25.0
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        output_button = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_output_folder_path,
            relief="flat"
        )
        output_button.place(
            x=301.0,
            y=226.0,
            width=26.0,
            height=25.0
        )

        button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        start_button = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.start_rebuild,
            relief="flat"
        )
        start_button.place(
            x=139.0,
            y=273.0,
            width=89.0,
            height=23.0
        )

        button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        help_button = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_instructions,
            relief="flat"
        )
        help_button.place(
            x=139.0,
            y=320.0,
            width=89.0,
            height=23.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()


    # Functions 
    def relative_to_assets(self, path: str) -> Path:
            return self.ASSETS_PATH / Path(path)


    def select_plugin(self):
        file_path = self.convert_path_for_powershell(filedialog.askopenfilename(filetypes=[("Unreal Engine Plugin", "*.uplugin")]))
        if file_path:
            self.plugin_path.set(file_path)


    def select_bat_file(self):
        target_version = self.convert_path_for_powershell(filedialog.askopenfilename(filetypes=[("Target Unreal Engine Version RunUAT.bat File", "*.bat")]))
        if target_version:
            self.target_version_runbat_file.set(target_version)

    def select_output_folder_path(self):
        output_path = self.convert_path_for_powershell(filedialog.askdirectory())
        if output_path:
            self.output_folder_path.set(output_path)

    def show_instructions(self):
        messagebox.showinfo("How To Use:", "To use,\n--First Select RunUAT.bat File   button and navigate to your target engine's RunUAT.bat file which should be in\n '\\TARGET_ENGINE_VERSION_FOLDER\\Engine\\Build\\BatchFiles\\'  folder. \n\n --You will then you will need to select .UPlugin File path.\n\n  --Then select Output Folder to save the converted plugin to.\n\n--Lastly, press the   Start Rebuild   button and wait.  ")


    def start_rebuild(self):
        plugin_path = self.plugin_path.get()
        target_version = self.target_version_runbat_file.get()
        output_path = self.output_folder_path.get()

        if (plugin_path and output_path and target_version):

            cmd = f'powershell -Command "& \'{self.target_version_runbat_file.get()}\' BuildPlugin -plugin=\'{self.plugin_path.get()}\' -package=\'{self.output_folder_path.get()}\'"'

            self.run_command(cmd)
        else:
            messagebox.showinfo("Error:", "All 3 paths must be set before proceeding.....")

    def run_command(self, cmd):
        try:
            subprocess.run(cmd, shell=True, check=True)
            messagebox.showinfo("Command:", "Finished running rebuild, check the command line to see if it succeeded.")
        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")


    def convert_path_for_powershell(self, path):
        converted_path = os.path.normpath(path)
        converted_path = converted_path.replace("\\", "\\\\")
        return converted_path
    



ui = UEPluginConv()