from tkinter import Text, Tk, Label, END

has_written = False
timer = 0


def count_down():
    global timer
    timer += 1
    if timer > 5:
        text.delete("1.0", END)
    root.after(1000, count_down)


def check_writing(event):
    global timer
    global has_written
    if has_written:
        timer = 0
    else:
        has_written = True
        count_down()


root = Tk()
root.title("Disappearing Text Writing App")
root.config(padx=40, pady=40, bg="#6FEDD6")
info = Label(text="Text will disappear after 5 seconds if you stop typing!!", bg='#FF1E1E', font=("Courier", 20, 'bold')
             , padx=10, pady=10, fg="white")
info.pack()
div = Label(width=100, bg="#6FEDD6")
div.pack()
text = Text(bg="#245953", fg='#F9F54B', width=60, height=10, font=("Courier", 20, 'bold'), pady=20, padx=20)
text.bind("<Key>", check_writing)
text.pack()
root.mainloop()
