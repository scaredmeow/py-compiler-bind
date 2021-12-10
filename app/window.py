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
    lexPane.insert(constants.END,"LEXEME\t\t\t\tTOKEN\n\n")
    for i in range(len(type)):
        lexPane.insert(constants.END,f'{str(value[i]) if len(str(value[i]))<=15 else str(value[i])[:10] + "..."}\t\t\t\t{str(type[i])}\n')
        # lexPane.insert(constants.END,f'{"" if type(value[i]) == int else ("" if True else "") }'
        #                              f'\t\t\t\t{str(type[i])}\n')


def print_error(error):                      # Print Text to Error Pane
    errorPane.config(state="normal")
    errorPane.delete('1.0', constants.END)
    for error in error:
        if error != '':
            errorPane.insert(constants.END,f'{error}\n')
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
window.configure(bg = "#251c3b")
canvas = Canvas(
    window,
    bg = "#251c3b",
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
    bg = "#2a2247",
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
    bg = "#2a2247",
    highlightthickness = 0,
    fg = "white",
    padx = 10,
    pady = 10,
    font = ("Consolas",10),
    state="disabled",)

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
    bg = "#2a2247",
    highlightthickness = 0,
    fg = "white",
    padx = 10,
    pady = 10,
    font = ("Consolas",10),
    state="disabled",)

errorPane.place(
    x = 26, y = 445,
    width = 531,
    height = 150)

background_img = PhotoImage(file = f"img/background.png")
background = canvas.create_image(
    469.5, 48.5,
    image=background_img)

img0 = PhotoImage(file = f"img/img0.png")            # Run Lexical Analyzer Button
lexButton = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_lex,
    relief = "flat",
    background= "#211b36",
    activebackground = "#211b36")

lexButton.place(
    x = 13, y = 52,
    width = 180,
    height = 30)

img1 = PhotoImage(file = f"img/img1.png")            # Run Semantic Analyzer Button
semButton = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat",
    background= "#211b36",
    activebackground = "#211b36")

semButton.place(
    x = 200, y = 52,
    width = 200,
    height = 30)

img2 = PhotoImage(file = f"img/img2.png")            # Bind Button
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = refresh,
    relief = "flat",
    background = "#099FD1",
    activebackground = "#099FD1")

b2.place(
    x = 20, y = 6,
    width = 100,
    height = 33)

window.resizable(False, False)
window.title("Bind Compiler")
window.mainloop()
