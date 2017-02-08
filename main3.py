from Tkinter import *
import os
from deploy_IBM import install_ibm
from deploy_IBM import deploy_ibm
from PIL import Image, ImageTk

""" heritage  pour frame """
class Application(Frame):

    """ la methode pour deplyer avec github et pour methode principale """

    def deploy_gitup(self):
        print self.github.get()
        deploy_ibm(git=self.github.get())

    """ la methode pour deplyer avec payh et pour methode principale """

    def line(self):
        os.system("pwd")
        deploy_ibm(path=self.path.get())
        os.system("pwd")

    """ la methode pour cree les widgets et appel des methode  """

    def createWidgets(self):

        w = Label(root, text="Cloud Fondrys Cloud ", font='Times 20 italic bold')
        w.grid(row=0, column=2)

        self.QUIT = Button()
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=1,column=3, sticky=NSEW)

        self.button_install = Button()
        self.button_install["text"] = "Install and config"
        self.button_install["command"] = install_ibm
        self.button_install.grid(row=2, column=3, sticky=NSEW)

        self.button_deploy = Button(root, text="Deploy with path", fg="black", command=self.line)
        self.button_deploy.grid(row=3, column=3, sticky=NSEW)

        self.button_deploy_git = Button(root, text="Deploy with git hub", fg="black", command=self.deploy_gitup)
        self.button_deploy_git.grid(row=4, column=3, sticky=NSEW)

        var_text = StringVar()
        self.path = Entry(root, textvariable=var_text, width=30)
        self.path.grid(row=1, column=2)


        var_text1 = StringVar()
        self.github = Entry(root, textvariable=var_text1, width=30)
        self.github.grid(row=2, column=2)

        var_text2 = StringVar()
        self.application_name = Entry(root, textvariable=var_text2, width=30)
        self.application_name.grid(row=3, column=2)

        Label(root, text='Enter le chmein de application').grid(row=1, column=1)
        Label(root, text='clone your application').grid(row=2, column=1)
        Label(root, text='Application name').grid(row=3, column=1)

        image = Image.open("ibmbluemix_logo.jpeg")
        photo = ImageTk.PhotoImage(image)

        label = Label(image=photo)
        label.image = photo
        label.grid(row=5, column=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        root.title('IBM_bluemix deploy')
        #self.grid(row=0, column=0, sticky=NSEW)
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()