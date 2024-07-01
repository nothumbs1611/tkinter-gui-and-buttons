from tkinter import *

window = Tk()
window.title("enter title")
window.minsize(width=500, height=500)

my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "new text"

# making buttons:

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    #my_label.config(text="Button got clicked!")
    my_label.config(text=new_text)
button = Button(text = "Click me", command=button_clicked)
button.pack()

input = Entry(width = 10)
input.pack()
input.get()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

def spinbox_used():
	# gets the current value in spinbox
	print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
	print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()



def checkbutton_used():
	# prints 1 if "on", 0 if 'off'
	print(checked_state.get())
checked_state = IntVar()
checkbutton=Checkbutton(text="is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
	print(radio_state.get())
# variable to hold on to which button is selected
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
#gets current selection from list
	print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
	listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

