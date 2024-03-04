import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left") #if you want to show the label on the window then you must have to write the pack function then it will print the statement on the GUI
#my_label.pack(expand=True) #the use of the expand is it will completely expand on the screen i.e. it will take the whole picture on the screen having equal space from the starting to bottom

import turtle
tim = turtle.Turtle()
tim.write("Some text", font=("Times nnew Roman", 80, "bold"))

window.mainloop()