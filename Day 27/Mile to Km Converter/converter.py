from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Arial", 12))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km, font=("Arial", 12))
calculate_button.grid(column=1, row=2)


window.mainloop()
