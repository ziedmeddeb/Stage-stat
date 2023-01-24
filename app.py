
from tkinter import filedialog
from tkinter import *
import customtkinter as c
import Stati


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")
def UploadAction(event=None):
    global filename
    filename = filedialog.askopenfilename(filetypes=(("CSV Files","*.csv"),))
    print('Selected:', filename)
    Stati.analyse(filename)


root = c.CTk()
root.geometry("600x500")
root.title("Analyse")
root.wm_iconbitmap('ico.ico')

label= c.CTkLabel(root,text="Veuillez insérer un fichier CSV")
label.place(relx=0.36,rely=0.1)

button = c.CTkButton(root, text='Open', command=UploadAction)
button.place(relx=0.5,rely=0.5 , anchor=CENTER)

root.mainloop()