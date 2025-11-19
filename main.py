import qrcode
import tkinter as tk
import tkinter.filedialog
from tkinter import *
from PIL import Image

icon_loaded = False

def Take_enter_input(event):
    INPUT = inputtxt.get("1.0", "end-1c")
    save_and_make_QR(INPUT)

def take_generate_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    save_and_make_QR(INPUT)

def take_generate_blank_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    save_and_make_with_icon_QR(INPUT)

def load_icon_input():
    global icon_filepath
    icon_filepath = tk.filedialog.askopenfilename()
    if icon_filepath:
        global icon_loaded
        icon_loaded = True
        print("icon loaded")

def clear_icon_input():
    global icon_loaded
    icon_loaded = False

def save_and_make_QR(text):
    img = qrcode.make(text, error_correction=qrcode.constants.ERROR_CORRECT_H)
    type(img)
    filename = tk.filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG", ".png"), ("JPEG", ".jpeg"), ("SVG", ".svg")])
    img.save(filename)
    inputtxt.delete("1.0", "end")

def save_and_make_with_icon_QR(text):
    img = qrcode.make(text, error_correction=qrcode.constants.ERROR_CORRECT_H)
    type(img)
    img = img.convert("RGBA")
    qr_width, qr_height = img.size
    square_size = int(qr_width * 0.25)
    white_square = Image.new('RGBA', (square_size, square_size), 'white')
    position = ((qr_width - square_size) // 2, (qr_height - square_size) // 2)
    img.paste(white_square, position)
    if icon_loaded:
        icon = Image.open(icon_filepath)
        icon_size = int(square_size*0.9)
        icon = icon.resize((icon_size, icon_size))
        icon_position = ((qr_width - icon_size) // 2, (qr_height - icon_size) // 2)
        img.paste(icon, icon_position)
    filename = tk.filedialog.asksaveasfilename(defaultextension='.png',
                                               filetypes=[("PNG", ".png"), ("JPEG", ".jpeg"), ("SVG", ".svg")])
    img.save(filename)
    inputtxt.delete("1.0", "end")


if __name__ == '__main__':
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    frame = tk.Frame(root)
    frame.grid(row=1, column=1)
    root.title("QR Code Generator")
    root.geometry("500x200")
    root.bind('<Return>', Take_enter_input)
    l = tk.Label(frame, text="Please insert text")
    inputtxt = Text(frame, height=1,
                    width=50)
    Generate = Button(frame, height=2,
                      width=20,
                      text="Generate",
                      command=lambda: take_generate_input())
    Generate_With_Icon = Button(frame, height=2,
                                width=20,
                                text="Generate with icon",
                                command=lambda: take_generate_blank_input())
    Load_Icon = Button(frame, height=2,
                                 width=20,
                                 text="Load icon",
                                 command=lambda: load_icon_input())
    Clear_Icon = Button(frame, height=2,
                        width=20,
                        text="Clear icon",
                        command=lambda: clear_icon_input())
    l.grid(column=0, row=0,columnspan=2)
    inputtxt.grid(column=0, row=1,columnspan=2, pady=10)
    Generate.grid(column=0, row=2)
    Generate_With_Icon.grid(column=1, row=2)
    Load_Icon.grid(column=0, row=3)
    Clear_Icon.grid(column=1, row=3)
    root.mainloop()

