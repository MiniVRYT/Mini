from tkinter import *
from tkinter.ttk import *
import os, sys
import tkinter as tk 



# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("PONG:Reimagined")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        startButton = Button(self, text="Classic",command=self.client_start)
        endButton = Button(self, text="Quit",command=self.quit_game)
        helpButton = Button(self, text="How To Play",command=self.how_to_play)
        # placing the button on my window
        startButton.place(x=160, y=200)
        endButton.place(x=160, y=260)
        helpButton.place(x=160, y=230)

       

    def client_start(self):
        os.system('python PONGMWIP.py')
        sys.exit()
    def quit_game(self):
        sys.exit()
    def how_to_play(self):
        os.system("notepad.exe ponghelp.txt.txt")
# root window created. Here, that would be the only window, but
# you can later have windows within windows.

root = Tk()

p1 = PhotoImage(file = 'ping-pong.png')
root.iconphoto(False, p1)

root.geometry("400x300")
 

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop() 
 