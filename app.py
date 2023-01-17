import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()

root.title("Text to Speech Converter")
root.geometry("900x500+200+200")
root.resizable(False,False)
root.configure(bg ="#455f96")

#defining functions
engine= pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_selection.get()
    speed = speed_selection.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == "Male"):
            engine.setProperty("voice",voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice",voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
           engine.setProperty("rate",250)
           setvoice()
        elif(speed == "Normal"):
            engine.setProperty("rate",150)
            setvoice()
        else: 
            engine.setProperty("rate",60)
            setvoice()

def download():
    text = text_area.get(1.0,END)
    gender = gender_selection.get()
    speed = speed_selection.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if(gender == "Male"):
            engine.setProperty("voice",voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty("voice",voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
           engine.setProperty("rate",250)
           setvoice()
        elif(speed == "Normal"):
            engine.setProperty("rate",150)
            setvoice()
        else: 
            engine.setProperty("rate",60)
            setvoice()

#UI
logo = PhotoImage(file="logo.png")
root.iconphoto(False,logo)

#frame
frame = Frame(root,bg="whitesmoke",width=900,height=100)
frame.place(x=0,y=0)

main_logo = PhotoImage(file="main_logo.png")
Label(frame,image=main_logo,bg="whitesmoke").place(x=10,y=5)

Label(frame,text= "TEXT TO SPEECH", font= "arial 20 bold",bg="whitesmoke",fg="black").place(x=100,y=30)


text_area = Text(root,font= "Robote 20",bg = "white", relief= GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font= "arial 15 bold",bg="#455f96",fg="white").place(x=580,y=160)
gender_selection = Combobox(root,values=['Male','Female'],font='arial 14',state= 'r',width=10)
gender_selection.place(x=550,y=200)
gender_selection.set('Male')

Label(root,text="SPEED",font= "arial 15 bold",bg="#455f96",fg="white").place(x=760,y=160)
speed_selection = Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state= 'r',width=10)
speed_selection.place(x=730,y=200)
speed_selection.set('Normal')


button = Button(root,text="Speak",width=10,font="arial 14 bold",bg="lightblue",fg="black",command=speaknow)
button.place(x=550,y=300)

button2 = Button(root,text="Download",width=10,font="arial 14 bold",bg= "lightgreen",fg="black",command= download)
button2.place(x=730,y=300)




root.mainloop()