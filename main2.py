from Tkinter import *
import os
from deploy import deploy
from deploy import install
from PIL import Image, ImageTk

""" heritage  pour frame """

class Application(Frame):

    """ la methode pour deplyer avec github et pour methode principale """

    def deploy_gitup(self):
        print self.github.get()
        deploy(git=self.github.get())

    """ la methode pour deplyer avec payh et pour methode principale """

    def line(self):
        os.system("pwd")
        deploy(path=self.path.get())
        os.system("pwd")

    """ la methode pour cree les widgets et appel des methode  """

    def createWidgets(self):

        w = Label(root, text="Heroku Cloud ", font='Times 20 italic bold')
        w.grid(row=0, column=2)

        self.QUIT = Button()
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=1,column=3, sticky=NSEW)

        self.hi_there = Button()
        self.hi_there["text"] = "Installer et configurer"
        self.hi_there["command"] = install
        self.hi_there.grid(row=2,column=3, sticky=NSEW)

        self.bouton_cliquer2 = Button(root, text="Deployer avec path", fg="black", command=self.line)
        self.bouton_cliquer2.grid(row=3, column=3, sticky=NSEW)

        self.bouton_cliquer3 = Button(root, text="Deployer avec github", fg="black", command=self.deploy_gitup)
        self.bouton_cliquer3.grid(row=4, column=3, sticky=NSEW)

        var_text = StringVar()
        self.path = Entry(root, textvariable=var_text, width=30)
        self.path.grid(row=1, column=2)


        var_text1 = StringVar()
        self.github = Entry(root, textvariable=var_text1, width=30)
        self.github.grid(row=2, column=2)

        var_text2 = StringVar()
        self.application_name = Entry(root, textvariable=var_text2, width=30)
        self.application_name.grid(row=3, column=2)

        Label(root, text=' chemin de application ').grid(row=1, column=1)
        Label(root, text=' clone application ').grid(row=2, column=1)
        Label(root, text=' nom de application ').grid(row=3, column=1)

        image = Image.open("heroku.png")
        photo = ImageTk.PhotoImage(image)

        label = Label(image=photo)
        label.image = photo
        label.grid(row=5, column=2)

    """ le constructeur """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.grid(row=0, column=0, sticky=NSEW)
        root.title('heroku cloud deploy')
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()