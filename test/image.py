import requests
import json
from PIL import Image, ImageTk
import os
from tkinter import Tk, Button, Canvas, PhotoImage
from datetime import datetime, timedelta

image_clear_sky = 'GITHUB/openImagePython/test/CLEAR_SKY.jpg'
image_few_clouds = 'GITHUB/openImagePython/test/FEW_CLOUDS.jpg'
image_scattered_cloud = 'GITHUB/openImagePython/test/SCATTERED_CLOUDS.jpg'
image_broken_clouds = 'GITHUB/openImagePython/test/BROKEN_CLOUDS.jpg'
image_light_rain = 'GITHUB/openImagePython/test/RAIN.jpg'
image_shower_rain = 'GITHUB/openImagePython/test/RAIN.jpg'
image_rain = 'GITHUB/openImagePython/test/RAIN.jpg'
image_thunderstorm = 'GITHUB/openImagePython/test/THUNDERSTORM.jpg'
image_snow = 'GITHUB/openImagePython/test/SNOW.jpg'
image_mist = 'GITHUB/openImagePython/test/SCATTERED_CLOUDS.jpg'

wheater_data = ''

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=48540063268e4840b02b778e58656233&q=caen&units=metric"
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
    print(" Temperature (in celsius unit) = " + str(current_temperature) + 
            "\n humidity (in percentage) = " + str(current_humidiy) +
            "\n description = " + str(weather_description))
            # "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
            # "\n description = " + str(weather_description) +
            # "\n longitude = " + str(current_lon) +
            # "\n latitude = " + str(current_lat))

if weather_description == 'clear sky':
    wheater_data = image_clear_sky

elif weather_description == 'few clouds':
    wheater_data = image_few_clouds

elif weather_description == 'broken clouds':
    wheater_data = image_broken_clouds

elif weather_description == 'scattered clouds':
    wheater_data = image_scattered_cloud

elif weather_description == 'shower rain':
    wheater_data = image_shower_rain

elif weather_description == 'rain':
    wheater_data = image_rain

elif weather_description == 'thunderstorm':
    wheater_data = image_thunderstorm

elif weather_description == 'snow':
    wheater_data = image_snow

elif weather_description == 'mist':
    wheater_data = image_mist

elif weather_description == 'light rain':
    wheater_data = image_rain

else :
    print('le temps ne correspond pas')

fenetre = Tk()
fenetre.attributes('-fullscreen', True)

w, h = fenetre.winfo_screenwidth(),fenetre.winfo_screenheight()

image = Image.open(wheater_data)
image = image.resize((w, h))

photo = ImageTk.PhotoImage(image)

can = Canvas(fenetre, highlightthickness=0)
can.create_image(0, 0, anchor='nw', image=photo)
can.pack(fill='both', expand=1)

Button(can,text='Quitter', command=fenetre.destroy).place(x=0, y=0)

fenetre.mainloop()

"""

while 1:
    print  = 'Run something..'

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)

"""

