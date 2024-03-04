from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.pack(side="left")
my_label.place(x=100, y=200)
my_label.grid(column=5, row=0)
my_label.config(padx=50, pady=50)

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text="My button got clicked")

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
print(input.get()) #for returning the string