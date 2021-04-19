import tkinter as tk
import requests
import math
import operator
import numpy as np


HEIGHT = 500
WIDTH = 600

root = tk.Tk()


expression = ""
expression_two = float()



def add(value):
    
    global expression
    expression += value
    print(expression)
    label_result['text'] = expression

def plastic_calculate():
    value = str(expression)
    result = eval(value)
    plastic_result = str(result * .25)  
    label_result['text'] = f' Your total is ${plastic_result[:4]} have a great day!'


def paper_calculate():
    value = str(expression)
    result = eval(value)
    paper_result = str(result * .20)
    label_result['text'] = f' Your total is ${(paper_result)[:4]} have a great day!'


def clear():
    global expression
    expression = ''
    label_result['text'] = (expression)

    



#FRAMES AND CANVAS

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#22c1c3')
frame.place( relx=0.0, rely=0.0, relwidth=1 , relheight=1)

#ENTRY CODE

#entry = tk.Entry(frame, bg="#dd1939", font=50)
#entry.place(rely=0.25, relx=0.25, relwidth=0.5, relheight=0.25)



#LABELS

label_result = tk.Label(frame,text="How many bags are you using?", font=40)
label_result.place( rely = 0.2, relwidth=1, relheight=0.25)


#BUTTONS

button_seven = tk.Button(frame, text="7", bg="Silver", command=lambda: add("7"))
button_seven.place( relx=0.25 , rely=0.55, relwidth=0.1)

button_eight = tk.Button(frame, text="8", bg="Silver", command=lambda: add("8"))
button_eight.place( relx=0.45, rely=0.55, relwidth=0.1)

button_nine = tk.Button(frame, text="9", bg="Silver", command=lambda: add("9"))
button_nine.place( relx=0.65, rely=0.55, relwidth=0.1)

button_four = tk.Button(frame, text="4", bg="Silver", command=lambda: add("4"))
button_four.place( relx=0.25 , rely=0.65, relwidth=0.1)

button_five = tk.Button(frame, text="5", bg="Silver", command=lambda: add("5"))
button_five.place( relx=0.45, rely=0.65, relwidth=0.1)

button_six = tk.Button(frame, text="6", bg="Silver", command=lambda: add("6"))
button_six.place( relx=0.65, rely=0.65, relwidth=0.1)

button_one = tk.Button(frame, text="1", bg="Silver", command=lambda: add("1"))
button_one.place( relx=0.25 , rely=0.75, relwidth=0.1)

button_two= tk.Button(frame, text="2", bg="Silver", command=lambda: add("2"))
button_two.place( relx=0.45, rely=0.75, relwidth=0.1)

button_three = tk.Button(frame, text="3", bg="Silver", command=lambda: add("3"))
button_three.place( relx=0.65, rely=0.75, relwidth=0.1)

button_zero= tk.Button(frame, text="0", bg="Silver", command=lambda: add("0"))
button_zero.place( relx=0.45, rely=0.85, relwidth=0.1)

button_plastic= tk.Button(frame, text="Plastic", bg="Silver", command=lambda: plastic_calculate())
button_plastic.place( relx=0, rely=0.85, relheight=0.15, relwidth=0.25)

button_paper= tk.Button(frame, text="Paper", bg="Silver", command=lambda: paper_calculate())
button_paper.place( relx=0.75, rely=0.85, relheight=0.15, relwidth=0.25)

clear_button= tk.Button(frame, text="Clear", bg="Silver", command=lambda: clear())
clear_button.place(relx=0.85, rely=0.65, relwidth=0.1)



root.mainloop()
                    

