import tkinter as tk

Height = 700
Width = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1 , relheight=1) #relx = 0.1 , rely = 0.1 centers item
button = tk.Button(frame, text = "Login", bg="Purple")
button.pack()

label = tk.Label(frame, text="This is a label", bg='yellow')
label.pack()

root.mainloop()