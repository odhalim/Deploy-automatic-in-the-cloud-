from Tkinter import *
import os
import time


def install_config():
    print ("hi there, everyone!")
    print 'install pyhton'
    os.system("python --version")
    print 'now installe virtualenv'
    # os.system("pip install virtualenv")
    # os.system("sudo apt-get install python-pip")
    print "pour interface heroku"
    os.system("heroku --version")

root = Tk()

message = Label(root, text="welcom to heroku cloud.")
message.grid()
        
bouton_quitter = Button(root, text="Quitter", command=quit)
bouton_quitter.grid(row=1,column=3)
        
bouton_cliquer = Button(root, text="install and config", fg="red",command=install_config)
bouton_cliquer.grid(row=2,column=3)

bouton_cliquer2 = Button(root, text="deploy", fg="red",command=quit)
bouton_cliquer2.grid(row=3,column=3)
        
var_text = StringVar()
txt = Entry(root, textvariable=var_text, width=30)
txt.grid(row=1,column=2)

var_text1 = StringVar()
txt1 = Entry(root, textvariable=var_text1, width=30)
txt1.grid(row=2,column=2)

var_text2 = StringVar()
txt2 = Entry(root, textvariable=var_text2, width=30)
txt2.grid(row=3,column=2)

Label(root, text='Enter application name').grid(row=1,column=1)
Label(root, text='clone yoyr application').grid(row=2,column=1)
Label(root, text='this one').grid(row=3,column=1)

#photo = PhotoImage(file='1.png')
#canvas = Canvas(root,width=200, height=200)
#canvas.create_image(0, 0, anchor=NW, image=photo)
#canvas.grid(row=1, column=1)

root.mainloop()
