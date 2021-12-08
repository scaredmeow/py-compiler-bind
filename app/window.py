import compiler
from tkinter import Tk
from tkinter import PhotoImage
from tkinter import Text
from tkinter import Canvas
from tkinter import Button
from tkinter import constants

 
def run_lex():                                  # Run Lexical Analyzer
    inputValue = inputPane.get("1.0","end-1c")
    lex = compiler.lexer(inputValue)
    print_lex(lex.type, lex.value)
    print_error(lex.error)
    lexPane.config(state="disabled")
    errorPane.config(state="disabled")

def print_lex(type,value):                      # Print Text to Lexical Pane
    lexPane.config(state="normal")
    lexPane.delete('1.0', constants.END)
    lexPane.insert(constants.END,"LEXEME\t\t\t\tTOKEN\n")
    # a = len(type)
    # print(a)
    # while a != -1:
    for i in range(len(type)):
        lexPane.insert(constants.END,f'{type[i]}\t\t\t\t{value[i]}\n')


def print_error(error):                      # Print Text to Error Pane
    errorPane.config(state="normal")
    errorPane.delete('1.0', constants.END)
    for error in error:
        if error != '':
            errorPane.insert(constants.END,f'{error}')
        else:
            continue

def refresh():
    inputPane.config(state="normal")
    lexPane.config(state="normal")
    errorPane.config(state="normal")
    inputPane.delete('1.0', constants.END)
    lexPane.delete('1.0', constants.END)
    errorPane.delete('1.0', constants.END)
    lexPane.config(state="disabled")
    errorPane.config(state="disabled")

window = Tk()

window.geometry("939x617")
window.configure(bg = "#211b36")
canvas = Canvas(
    window,
    bg = "#211b36",
    height = 617,
    width = 939,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

inputPane_img = PhotoImage(file = f"img/img_textBox0.png")
inputPane_bg = canvas.create_image(
    291.5, 272.0,
    image = inputPane_img)

inputPane = Text(
    bd = 0,
    bg = "#261d3d",
    highlightthickness = 0,
    fg = "white",
    padx = 10,
    pady = 10,
    font = ("Consolas",10),)

inputPane.place(
    x = 26, y = 110,
    width = 531,
    height = 322)

lexPane_img = PhotoImage(file = f"img/img_textBox1.png")
lexPane_bg = canvas.create_image(
    740.5, 353.5,
    image = lexPane_img)

lexPane = Text(
    bd = 0,
    bg = "#261d3d",
    highlightthickness = 0,
    fg = "white",
    padx = 10,
    pady = 10,
    font = ("Consolas",10),
    )

lexPane.place(
    x = 568, y = 110,
    width = 345,
    height = 485)

errorPane_img = PhotoImage(file = f"img/img_textBox2.png")
errorPane_bg = canvas.create_image(
    291.5, 521.0,
    image = errorPane_img)

errorPane = Text(
    bd = 0,
    bg = "#261d3d",
    highlightthickness = 0,
    fg = "white",
    padx = 10,
    pady = 10,
    font = ("Consolas",10),
    )

errorPane.grid(row=0, column=0, sticky='ew')

errorPane.place(
    x = 26, y = 445,
    width = 531,
    height = 150)

background_img = PhotoImage(file = f"img/background.png")
background = canvas.create_image(
    469.5, 48.5,
    image=background_img)

img0 = PhotoImage(file = f"img/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_lex,
    relief = "flat",
    activebackground = "#211b36")

b0.place(
    x = 21, y = 52,
    width = 179,
    height = 30)

img1 = PhotoImage(file = f"img/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    activebackground = "#211b36")

b1.place(
    x = 214, y = 52,
    width = 202,
    height = 30)

img2 = PhotoImage(file = f"img/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    background= "#099FD1",
    command = refresh,
    activebackground = "#099FD1")

b2.place(
    x = 15, y = 6,
    width = 72,
    height = 33)



window.resizable(False, False)
window.title("Bind Compiler")
window.mainloop()
