import qrcode
import tkinter as tk
import tkinter.filedialog
from tkinter import *

def Take_enter_input(event):
    INPUT = inputtxt.get("1.0", "end-1c")
    save_and_make_QR(INPUT)

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    save_and_make_QR(INPUT)


def save_and_make_QR(text):
    img = qrcode.make(text)
    type(img)
    filename = tk.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG", ".png"), ("JPEG", ".jpeg"), ("SVG", ".svg")])
    img.save(filename)
    inputtxt.delete("1.0", "end")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("500x100")
    root.bind('<Return>', Take_enter_input)
    l = tk.Label(root, text="Please insert text")
    inputtxt = Text(root, height=1,
                    width=50)
    Generate = Button(root, height=2,
                     width=20,
                     text="Generate",
                     command=lambda: Take_input())
    l.pack()
    inputtxt.pack()
    Generate.pack()
    root.mainloop()

