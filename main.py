###########################################################
# Created by Timothé Montfrond
# Licence: None
# Please don't remove anything that's mention me
###########################################################





###########################################################
# Imports of librarys
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import os, webbrowser, customtkinter, json
###########################################################
# Def of some commands

PATH = os.path.dirname(os.path.realpath(__file__))

def open_local_file():
    os.startfile(os.getcwd())

def about_frame():
    about_w = Tk(className= " About PGR Launcher")
    about_w.geometry("400x100")
    about_w.resizable(False, False)
    about_label1 = Label(about_w, text="PGR Launcher is dev by one person: \n Timothe Montfrond \n\n Licence: None", justify=CENTER, font=('Arial 13 bold'))
    about_label1.pack()

def help_page():
    webbrowser.open("https://www.python.org/")

###########################################################
# Load/Read of the config.json file which is the file with the all path and parameters needed for the launcher

with open("config.json") as config:
    configList = json.load(config)
    config.close()

path_exec = configList['1']
bullshit = configList['2']

key = ""

def print_value():
    print(path_exec)

###########################################################
# Generate window
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("System")
root = customtkinter.CTk(className=' PGR Launcher - Template')
root.iconbitmap('icon.ico')
root.geometry("900x500")
root.resizable(False, False)

# Content
bg = PhotoImage(file='main_icon.png')
icon = ImageTk.PhotoImage(Image.open(PATH + "/icon.png").resize((50, 50), Image.ANTIALIAS))
main_icon = ImageTk.PhotoImage(Image.open(PATH + "/main_icon.png").resize((700, 250), Image.ANTIALIAS))
canvas = Canvas(root, width=700, height=250, bd=0)
canvas.create_image(350, 125, image=main_icon, anchor=CENTER)
canvas.place(anchor=CENTER, relx=.5, rely=.3)

play_button = customtkinter.CTkButton(root, text="Play", height=50, width=400, corner_radius=10, command=root.destroy)
play_button.place(anchor=CENTER, relx=.5, rely=.65)

files_button = customtkinter.CTkButton(text="Local Files", height=50, width=400, corner_radius=10, command=open_local_file)
files_button.place(anchor=CENTER, relx=.5, rely=.79)

quit_button = customtkinter.CTkButton(text="Quit", height=50, width=400, corner_radius=10, fg_color="#C70039", hover_color="#FF1357", command=root.destroy)
quit_button.place(anchor=CENTER, relx=.5, rely=.93)

about_button = customtkinter.CTkButton(text="", image=icon, command=about_frame, width=50, height=50)
about_button.place(anchor=CENTER, relx=.04, rely=.93)

one_button = customtkinter.CTkButton(text="1", command=print_value, width=50, height=50)
one_button.pack()


root.mainloop()
###########################################################