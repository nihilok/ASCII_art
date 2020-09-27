import os
from tkinter import *
from tkinter import filedialog
import pyperclip

import ascii_art


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
root.minsize(1024, 768)
root.title('Image to ASCII converter')
root.iconbitmap(resource_path('icon.ico'))


class MainWindow:
    def __init__(self, master):
        button_frame = Frame(master)
        button_frame.pack(pady=5)
        size_label = Label(button_frame, text="Desired height in lines:")
        size_label.pack(side='left', fill='y')
        self.s = StringVar()
        self.s.set(90)
        self.d_edit = Entry(button_frame, text=self.s, width=5)
        self.d_edit.pack(side='left', fill='y')
        choose = Button(button_frame, text='Choose an image', command=self.get_file)
        choose.pack(side='left', padx=2)
        spacer = Label(button_frame, width=30)
        spacer.pack(side='left', fill='x', expand=True)
        self.copy = Button(button_frame, text='Copy text', command=self.copy_text, state='disabled')
        self.copy.pack(side='left')
        self.save = Button(button_frame, text='Save text', command=self.save_text, state='disabled')
        self.save.pack(side='left')
        self.label = Label(root, text='Choose an image...', justify='left', font='Courier 12')
        self.label.pack(pady=2, padx=20, fill='both', expand=True)

    def get_file(self):
        desired_height = int(self.d_edit.get())
        filename = filedialog.askopenfilename(initialdir="/", title="Select image", filetypes=(
            ("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        if filename:
            self.label.config(text=ascii_art.main(filename, desired_height), font='Courier 6')
            self.copy.config(state='normal')
            self.save.config(state='normal')
        else:
            pass

    def copy_text(self):
        pyperclip.copy(self.label['text'])

    def save_text(self):
        with open(f'ascii_image_{ascii_art.date_stamp()}.txt', 'w') as f:
            f.write(self.label['text'])


if __name__ == "__main__":

    mw = MainWindow(root)

root.mainloop()
