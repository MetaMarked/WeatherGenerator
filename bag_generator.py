import math
import operator
import numpy as np
import tkinter as tk

root = tk.Tk

Height = 500
Width = 600

canvas = tk.Canvas(root, Height=Height , width=Width)
canvas.pack()

        
def bag_count():
    Plastic = 0.20
    Paper = 0.50
    while True:

        print("What type of bag will you be using today?")
        answer = input()
        
        if answer == "Plastic" or "plastic":
            print("How many bags?")
            num_input = float(input())
            plastic_total = float(num_input * (Plastic))
            print(f'Your total is {plastic_total}, please proceed to scan')
            break
        

        elif answer == "paper" or "Paper":
            print("How many bags?")
            num_input = float(input())
            paper_total = float(num_input * (Paper))
            print(paper_total, f'Proceed to scan')
            break
        
        else:
            print("Proceed to scan")
        break    

bag_count()
root.mainloop()               
                    
                    
