import tkinter as tk
import requests

HEIGHT = 700
WIDTH = 800
def click_function(entry):
    print("This is the Entry", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = str(name) + ' ' + str(desc)  + ' ' + str(temp)
    except:
        final_str = 'Issue retrieving data'

    return final_str

def get_weather(city):
    weather_key = '095fcdb87072ac6fb7fa52a4426987d6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, "q": city, 'units': "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    
root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='DragonDive.png') 
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#d12dfd', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75 , relheight=0.1, anchor='n') #relx = 0.1 , rely = 0.1 centers item

entry = tk.Entry(frame, bg='light blue', font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text = "Get Weather", bg="Purple", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#d12dfd', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75 , relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text= "Search a City" , bg='light blue')
label.place( relwidth=1, relheight=1)

root.mainloop()