import requests
import json
from PIL import Image, ImageTk
import os
from tkinter import Tk, Button, Canvas, PhotoImage


image_clear_sky = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_fews_clouds = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_scattered_cloud = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_broken_clouds = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_shower_rain = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_rain = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_thunderstorm = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_snow = 'GITHUB/openImagePython/test/SOLEIL2.png'
image_mist = 'GITHUB/openImagePython/test/SOLEIL2.png'


base_url = "http://api.openweathermap.org/data/2.5/weather?appid=48540063268e4840b02b778e58656233&q=redene,fr&units=metric"
complete_url = base_url

response = requests.get(complete_url) 

x = response.json() 

if x["cod"] != "404": 
  
    y = x["main"] 
    current_temperature = y["temp"]  
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"] 
    c = x["coord"]
    current_lon = c["lon"]
    current_lat = c["lat"]
  
    # print following values 
    print(" Temperature (in celsius unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description) +
          "\n longitude = " +
                    str(current_lon) +
          "\n latitude = " +
                    str(current_lat))

if weather_description == 'light rain':
    
    fenetre = Tk()
    fenetre.attributes('-fullscreen', True)

    w, h = fenetre.winfo_screenwidth(),fenetre.winfo_screenheight()

    image = Image.open(image_clear_sky)
    image = image.resize((w, h))

    photo = ImageTk.PhotoImage(image)

    can = Canvas(fenetre, highlightthickness=0)
    can.create_image(0, 0, anchor='nw', image=photo)
    can.pack(fill='both', expand=1)

    Button(can,text='Quitter', command=fenetre.destroy).pack()

    fenetre.mainloop()
else :
    print('trop froid')


