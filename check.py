import sys
import os
import Tkinter
from distutils.core import setup
from tkMessageBox import showinfo
from threading import Thread
from Tkinter import *

master = Tk()
master.minsize(100, 100)
#master.geometry("320x100")
f = Frame(master)

def callback_threaded1():
    Thread(target=helloCallBack).start()

def callback_threaded2():
    Thread(target=gettest).start()

def callback_threaded3():
    Thread(target=getrecognizer).start()
	
def helloCallBack():
    os.system('python datasetgen.py')


def gettest():
    os.system('python trainset.py')


def getrecognizer():
    os.system('python recogniser.py')
	
def getrecognizer1():
    os.system('python recogniser1.py')


B = Button(master, text="DATASET", height=5, width=10, command=callback_threaded1)
Button1 = Button(master, text="TRAIN", height=5, width=10, command=callback_threaded2)
Button2 = Button(master, text="RECOGNISE", height=5, width=10, command=callback_threaded3)
B.pack(side=LEFT, padx=20)
Button1.pack(padx=20, side=LEFT)
Button2.pack(padx=20, side=LEFT)
master.mainloop()
