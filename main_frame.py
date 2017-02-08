from Tkinter import *
import os
from PIL import Image, ImageFont, ImageDraw, ImageTk


def run_heroku():
    os.system('python main2.py')

def run_bluemix():
    os.system('python main3.py')

def readme():
    os.system("gedit redme.txt")



fenetre=Tk()
cadre = Frame(fenetre, width=300, height=100, borderwidth=1)
cadre.grid()

#bouton_cliquer2 = Button(cadre, text="Deploy with path", fg="black", command=quit)
#bouton_cliquer2.grid(row=1, column=1)

#menu_bar
menubar = Menu(fenetre)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=readme)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=filemenu)

image = Image.open("5.png")
photo = ImageTk.PhotoImage(image)

Butt = Button(image=photo, command=run_heroku)
Butt.image = photo
Butt.grid(row=0, column=0, sticky=NSEW)

image2 = Image.open("6.png")
photo1 = ImageTk.PhotoImage(image2)

Butt = Button(image=photo1, command=run_bluemix)
Butt.image2 = photo1
Butt.grid(row=1, column=0, padx=2, pady=4, columnspan=9, sticky=NSEW)

image3 = Image.open("3.png")
photo2 = ImageTk.PhotoImage(image3)

Butt = Button(image=photo2, command=quit)
Butt.image3 = photo1
Butt.grid(row=2, column=0, padx=2, pady=4, columnspan=9, sticky=NSEW)

image4 = Image.open("9.png")
photo3 = ImageTk.PhotoImage(image4)

Butt = Button(image=photo3, command=quit)
Butt.image4 = photo1
Butt.grid(row=3, column=0, padx=2, pady=4, columnspan=9, sticky=NSEW)

fenetre.config(menu=menubar)
fenetre.mainloop()
