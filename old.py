from tkinter import *
from tkinter import filedialog
import ascii_art
import pyperclip


def get_file():
    desired_height = int(d_edit.get())
    filename = filedialog.askopenfilename(initialdir="/", title="Select image", filetypes=(
    ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    if filename:
        label.config(text=ascii_art.main(filename, desired_height), font='Courier 6')
    else:
        pass


def copy_text():
    pyperclip.copy(label['text'])


def save_text():
    with open(f'ascii_image_{ascii_art.date_stamp()}.txt', 'w') as f:
        f.write(label['text'])


root = Tk()
root.minsize(1024, 768)
root.title('Image to ASCII text converter')
root.iconbitmap('icon.ico')

button_frame = Frame(root)
button_frame.pack(pady=10)
size_label = Label(button_frame, text="Desired height in lines:")
size_label.pack(side='left', fill='y')
s = StringVar()
s.set(90)
d_edit = Entry(button_frame, text=s, width=5)
d_edit.pack(side='left', fill='y')
choose = Button(button_frame, text='Choose an image', command=get_file)
choose.pack(side='left', padx=2)
spacer = Label(button_frame, width=30)
spacer.pack(side='left', fill='x', expand=True)
copy = Button(button_frame, text='Copy text', command=copy_text)
copy.pack(side='left')
save = Button(button_frame, text='Save text', command=save_text)
save.pack(side='left')

label = Label(root, text='Choose an image...', justify='left', font='Courier 12')
label.pack(pady=20, padx=20, fill='both', expand=True)

root.mainloop()
