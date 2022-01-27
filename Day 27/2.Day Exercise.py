from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = nw_input.get()
    my_label.config(text=new_text)

    
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="New Button")
button.grid(column=1, row=1)
button2.grid(column=2, row=0)

# Entry
nw_input = Entry(width=10)
print(nw_input.get())
nw_input.grid(column=3, row=2)


window.mainloop()
