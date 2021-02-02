import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background_image= tk.PhotoImage(file='DragonDive.png') 
#background_label= tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#d12dfd', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75 , relheight=0.1, anchor='n') #relx = 0.1 , rely = 0.1 centers item

entry = tk.Entry(frame, bg='light blue', font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", bg="Purple")
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#d12dfd', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75 , relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="This is a label", bg='light blue')
label.place( relwidth=1, relheight=1)

root.mainloop() 