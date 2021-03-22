from tkinter import *
import tkinter.messagebox
from tkinter import filedialog


def empty_func():
    # Code to be written
    pass


def about_func():
    tkinter.messagebox.showinfo('About Us', 'Working in progress')


def browse_file():
    file_name = filedialog.askopenfilename()
    print(file_name)


root = Tk()
root.geometry('900x600')
root.title('GUI with Tkinter')

# Menu ********************************************************
# Main Menu
main_menu = Menu(root)

# Menu 1
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=browse_file)
file_menu.add_command(label="Save", command=empty_func)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
main_menu.add_cascade(label="File", menu=file_menu)

# Menu 2
tool_menu = Menu(main_menu, tearoff=0)
tool_menu.add_command(label="Find", command=empty_func)
tool_menu.add_command(label="Debugger", command=empty_func)
tool_menu.add_command(label="Replace", command=empty_func)
main_menu.add_cascade(label="Tools", menu=tool_menu)

# Menu 3
tool_menu = Menu(main_menu, tearoff=0)
tool_menu.add_command(label="Documentation", command=empty_func)
tool_menu.add_command(label="About", command=about_func)
main_menu.add_cascade(label="Help", menu=tool_menu)
# End Menu *****************************************************

# Frame ********************************************************
frame = Frame(root)
frame.pack()

label = Label(frame, text="Hello world")
label.pack()

# LEFT FRAME
left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=10)

label1 = Label(left_frame, text="Left Frame")
label1.pack(padx=3, pady=3)

button1 = Button(left_frame, text="Button1")
button1.pack(padx=3, pady=3)
button2 = Button(left_frame, text="Button2")
button2.pack(padx=3, pady=3)

# RIGHT FRAME
right_frame = Frame(root)
right_frame.pack(side=RIGHT, padx=10)

label2 = Label(right_frame, text="Right Frame")
label2.pack(padx=3, pady=3)

button3 = Button(right_frame, text="Button3")
button3.pack(padx=3, pady=3)

# FIXED FRAME
fixed_frame = Frame(root)
fixed_frame.pack(padx=50, pady=50)

label3 = Label(fixed_frame, text="Fixed Frame")
label3.pack(padx=3, pady=3)

button4 = Button(fixed_frame, text="Button4")
button4.pack(side=LEFT, padx=5)
button5 = Button(fixed_frame, text="Button5")
button5.pack(side=LEFT, padx=5)
button6 = Button(fixed_frame, text="Button6")
button6.pack(side=LEFT, padx=5)

# BOTTOM FRAME
bottom_frame = Frame(root, bd=1, bg='#add8e6')
bottom_frame.pack()

button7 = Button(bottom_frame, text="Button7")
button7.grid(row=0, column=0)
button8 = Button(bottom_frame, text="Button8")
button8.grid(row=1, column=1)
button9 = Button(bottom_frame, text="Button9")
button9.grid(row=2, column=2)
label4 = Label(bottom_frame, text="Label in Bottom Frame using *Grid")
label4.grid(row=4, column=1)
# END Frames ******************************************************

root.config(menu=main_menu)
root.mainloop()
