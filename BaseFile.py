# importing required modules
import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg

class note:

    def __init__(self):
        # delclaring self.root variable as Tk() and formating it
        self.root=Tk()
        self.root.geometry("1366x768")
        self.name = "Untitled"
        self.root.title(f"{self.name} - JAVA APPLET RUNNER by Nikhil")

        self.tx = Text(self.root, undo=True, font=("Helvetica", 20))
        self.tx.pack(expand=True, fill=BOTH)

        # declartion of mainmenu of the program

        mainmenu = Menu(self.root)

        # declartion of first menu named as m1(file)
        m1 = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="File", font=("BOLD", 15), menu=m1)
        m1.add_command(label="New File", font=("BOLD", 15), command=self.newFile)
        m1.add_command(label="Open", font=("BOLD", 15), command=self.openFile)
        m1.add_command(label="Save", font=("BOLD", 15), command=self.saveFile)
        m1.add_command(label="Save as", font=("BOLD", 15), command=self.saveasFile)
        m1.add_command(label="find", font=("BOLD", 15), command=self.find)
        m1.add_command(label="Exit", font=("BOLD", 15), command=self.exit1)

        # declartion of first menu named as m2(edit)

        m2 = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Edit", font=("BOLD", 15), menu=m2)
        m2.add_command(label="Undo", font=("BOLD", 15), command=self.tx.edit_undo)
        m2.add_command(label="Redu", font=("BOLD", 15), command=self.tx.edit_redo)
        m2.add_separator()
        m2.add_command(label="Cut", font=("BOLD", 15), command=self.cut)
        m2.add_command(label="Copy", font=("BOLD", 15), command=self.copy)
        m2.add_command(label="Paste", font=("BOLD", 15), command=self.paste)

        # declartion of third menu named as m3 (view)
        m3 = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="View", font=("BOLD", 15), menu=m3)
        m3.add_command(label="Vertical", font=("BOLD", 15), command=self.Vertical)
        m3.add_command(label="Horizontal", font=("BOLD", 15), command=self.Horizontal)
        m3.add_command(label="customized", font=("BOLD", 15), command=self.customized)

        # declartion of first menu named as m4(help)
        m4 = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Help", font=("BOLD", 15), menu=m4)
        m4.add_command(label="About Notepad", font=("BOLD", 15), command=self.help)

        m5 = Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="Run java", font=("BOLD", 15), menu=m5)
        m5.add_command(label="run", command=self.runJava)
        # configering the mainmenu
        self.root.config(menu=mainmenu)

        # scrollbar for text area if there is a lot of text in there
        scy = Scrollbar(self.tx, relief=RAISED, width=25,)
        scy.pack(side=RIGHT, fill=Y)
        scy.config(command=self.tx.yview)
        self.tx.config(yscrollcommand=scy.set)

        # mainloop for infinite screeen entries
        self.root.mainloop()

    # this funtion for 'Apply' button in customized function
    def update(self):
        self.root.geometry(f"{self.h.get()}x{self.w.get()}")



    # thisfunction for view ->  customized function
    def customized(self):
        new = Frame(self.root, height=140, width=200, bg="light blue")
        new.place(x=50, y=50)

        Label(new, text="Height", bg="light blue").place(x=10, y=30)
        Label(new, text="Width", bg="light blue").place(x=10, y=60)
        Entry(new, textvariable=self.h).place(x=70, y=30)
        Entry(new, textvariable=self.w).place(x=70, y=60)
        Button(new, text="Apply", command=self.update).place(x=80, y=100)
        Button(new, text="X", command=new.destroy, width=2,).place(x=170, y=5)

    # this function is for view -> vertical menu
    def Vertical(self):
        self.root.geometry("683x768")

    # this function is for view -> horizontal menu
    def Horizontal(self):
        self.root.geometry("1366x384")

    # this function is for file -> new file menu
    def newFile(self):
        # print("created new file")
        output = tmsg.askyesnocancel(
            "Notepad By Nikhil", "Do want to save this file?")
        if (output == YES):
            self.save()
            self.tx.delete(1.0, END)
        else:
            self.root.title(f"{self.name} - Notepad by Nikhil")
            self.tx.delete(1.0, END)
            self.save()
        tmsg.showinfo("Information","created new file")


    # this function is for file -> savefile menu
    def save(self):

        self.file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), (
            "Python Files", "*.py"), ("C files", "*.c"), ("C++ files", "*.cpp")], initialfile="Untitled.txt")
        if self.file == "":
            self.file = None
        else:
            f = open(self.file, "w")
            f.write(self.tx.get(1.0, END))
            f.close()
            # this is for if you cancelled save pop up for any reason 
        try :
            self.name = os.path.basename(self.file)
            self.root.title(f"{self.name} - Notepad by Nikhil")
        except:
            # pass
            tmsg.showerror("Error","Your file is note saved!!")


    def saveasFile(self):
        self.save()


    def saveFile(self):
        # test=
        # print(self.name)
        if self.name == "Untitled":
            self.save()
        else:
            f = open(self.file, "w")
            f.write(self.tx.get(1.0, END))
            f.close()
            tmsg.showinfo("file appended","Your file is saved again")


    def runJava(self):
        print("Running applet......")
        self.saveFile()
            # print(cmd1+"\n"+cmd2)
        # print(self.name+"in block1")
        # print(os.path.baseself.name(file))
        os.system(f'javac {os.path.basename(self.file)}')
        os.system(f'appletviewer {os.path.basename(self.file)}')

        print("Exited applet")

    # this function is for file -> open file menu


    def openFile(self):
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[(
            "All files", "*.*"), ("Text Documents", "*.txt"), ("Python files", "*.py")])
        if file == "":
            file = None
        else:
            self.root.title(os.path.basename(file)+" - Notepad by Nikhil")
            self.tx.delete(1.0, END)
            f = open(file, "r")
            self.tx.insert(1.0, f.read())
            f.close()

    # this function is for file -> saveas file menu


    # this function is for edit -> cut menu
    def cut(self):
        self.tx.event_generate(("<<Cut>>"))

    # this function is for edit -> copy menu


    def copy(self):
        self.tx.event_generate(("<<Copy>>"))

    # this function is for edit -> paste menu


    def paste(self):
        self.tx.event_generate(("<<Paste>>"))

    # this function is for file-> find menu


    def find(self):
        # global findVar
        # global fr
        self.fr = Frame(height=60, width=220, bg="light Gray")
        self.fr.place(x=800, y=100)
        self.findVar = StringVar()
        Button(self.fr, text="FIND", bg="light gray",
            relief=GROOVE, command=self.getin).place(x=10, y=3)
        Entry(self.fr, textvariable=self.findVar, bg="light Gray").place(x=60, y=5)
        Button(self.fr, text="X", command=self.fr.destroy).place(x=200, y=3)

    # this fumctom is for button  in 102 th line for searching ccorsponding string to entire text


    def getin(self):
        strr = self.tx.get(1.0, END)
        cha = strr.find(self.findVar.get())
        dis = Label(
            self.fr, text=f"{self.findVar.get()} is found at {cha}th character", bg="pink")
        dis.place(x=10, y=35)
        dis.after_cancel(400)


    # this function is for help -> about us menu
    def help(self):
        a = tmsg.showinfo("About Notepad", "Hi There I am Nikhil Maurya I am currently purssuing BCA from Dr. Virendra Swarup institute of computer studies this project is a extened version of Notepad by Nikhil start Date = 25/12/2022.The finishing date is 28/12/2022. This is a simulation progrram of Microsoft't Windows Buit in Basic text editor called \"Notepad\" and an added feature of running java applet.\tHow it works??.....read discription on repository\'\n\n\n\tThank you for using it. \n\n")

    # this funtion is for file -> exit menu


    def exit1():
        exit()


    
#driver code 
toor=note()

