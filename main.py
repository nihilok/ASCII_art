from tkinter import *
from tkinter import filedialog
import ascii_art
import pyperclip


def get_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select image", filetypes=(
    ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    if filename:
        label.config(text=ascii_art.main(filename), font='Courier 6')
    else:
        pass


def copy_text():
    pyperclip.copy(label['text'])


def save_text():
    with open(f'ascii_image_{ascii_art.date_stamp()}.txt', 'w') as f:
        f.write(label['text'])


root = Tk()
root.minsize(800, 600)
root.title('Image to ASCII text converter')

root.iconbitmap('icon.ico')

label = Label(root, text='Choose an image...', justify='left', font='Courier 12')
label.pack(pady=20, padx=20, fill='both', expand=True)
button_frame = Frame(root)
button_frame.pack()
choose = Button(button_frame, text='Choose an image', command=get_file)
choose.pack(side='left', pady=20)
copy = Button(button_frame, text='Copy text', command=copy_text)
copy.pack(side='left', pady=2)
save = Button(button_frame, text='Save text', command=save_text)
save.pack(side='left')
root.mainloop()