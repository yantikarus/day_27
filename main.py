from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    converted_answer = round(int(input.get())*1.609, 2)
    answer.config(text=str(converted_answer))


#entry
input = Entry(width=5)
input.grid(row=0, column=1)


#Label
# my_label = Label(text="I am a label", font=("roboto", 24, "bold"))
# my_label.config(text="Bubuci")
# my_label.grid(row=0, column=0)

miles_label = Label(text="Miles", font=("roboto", 20))
miles_label.grid(row=0, column=2)

equal = Label(text="is equal to", font=("roboto", 20))
equal.grid(row=1, column=0)

answer = Label(text="0", font=("roboto", 20))
answer.grid(row=1, column=1)

km = Label(text="km", font=("roboto", 20))
km.grid(row=1, column=2)

#Button
# button = Button(text="love me", command=button_clicked)
# new_button = Button(text="im new", command=button_clicked)
# new_button.grid(row=0, column=2)
# button.grid(row=1, column=1)

calculate_btn = Button(text="Calculate", command=button_clicked)
calculate_btn.grid(row=2, column=1)








window.mainloop()
