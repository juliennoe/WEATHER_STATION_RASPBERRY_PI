#LIBRARY
import requests
import json
from PIL import Image, ImageTk
import os
from tkinter import Tk, Button, Canvas, PhotoImage
from datetime import datetime, timedelta
import pytz
import schedule
import time
import sys
import serial
from lcdbackpack import LcdBackpack

#LCD CONFIGUTATION WITH LCDBACKPACK
lcd = LcdBackpack('/dev/ttyACM0', 115200)
lcd.connect()
lcd.clear()

lcd.set_autoscroll(True)
lcd.set_cursor_home()

LCD_COLS = 16
LCD_ROWS = 2

lcd.set_lcd_size(LCD_COLS, LCD_ROWS)
os.system("python clear_screen.py")

#IMAGE REFERENCE PATH
main_path = "/home/pi/"
image_clear_sky = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/CLEAR_SKY.jpg'
image_few_clouds = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/FEW_CLOUDS.jpg'
image_scattered_cloud = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/SCATTERED_CLOUDS.jpg'
image_broken_clouds = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/BROKEN_CLOUDS.jpg'
image_light_rain = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/RAIN.jpg'
image_shower_rain = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/RAIN.jpg'
image_rain = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/RAIN.jpg'
image_thunderstorm = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/THUNDERSTORM.jpg'
image_snow = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/SNOW.jpg'
image_mist = main_path +'GITHUB/openImagePython/MainProject/REF_WHEATER_IMAGES/SCATTERED_CLOUDS.jpg'

#WHEATER_API_INFO
wheater_data = ''
city_name = input("Meteo pour quelle ville ?:")
api_key = "48540063268e4840b02b778e58656233"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

print(complete_url)


#WHEATER_FUNCTION
def update_weather():

    #JSON_REQUEST
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
  
        tz_paris = pytz.timezone('Europe/Paris')
        now = datetime.now(tz_paris)
        current_time = now.strftime('%H:%M:%S')
        print("Heure actuelle = ", current_time)

        #PRINT_FOLLOW_VALUES
        print(" Temperature (in celsius unit) = " + str(current_temperature) + 
            "\n humidity (in percentage) = " + str(current_humidiy) +
            "\n description = " + str(weather_description))
            # "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
            # "\n description = " + str(weather_description) +
            # "\n longitude = " + str(current_lon) +
            # "\n latitude = " + str(current_lat))
   
    # WRITE DATA ON LCD SCREEN
    lcd.write("degres: " + str(current_temperature) + 
            "\rhumidity: " + str(current_humidiy) +
            "\rcity: " + str(city_name))

    # CHANGE LCD COLOR WITH TEMPERATURE
    if current_temperature < 15:
        lcd.set_backlight_blue()
    if current_temperature > 15:
        lcd.set_backlight_green()
    if current_temperature > 27:
        lcd.set_backlight_red()
  

    #CHOOSE_IMAGE_PRISM
    if weather_description == 'clear sky':
        wheater_data = image_clear_sky

    elif weather_description == 'few clouds':
        wheater_data = image_few_clouds

    elif weather_description == 'broken clouds':
        wheater_data = image_broken_clouds
    
    elif weather_description == 'overcast clouds':
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
        print('fail type weather')

    #WINDOW_CREATION_FULL_SIZE
    fenetre = Tk()
    fenetre.attributes('-fullscreen', True)
    print(wheater_data)

    w, h = fenetre.winfo_screenwidth(),fenetre.winfo_screenheight()

    image = Image.open(wheater_data)
    image = image.resize((w, h))

    photo = ImageTk.PhotoImage(image)

    can = Canvas(fenetre, highlightthickness=0)
    can.create_image(0, 0, anchor='nw', image=photo)
    can.pack(fill='both', expand=1)

    Button(can,text='EXIT', command=fenetre.destroy).place(x=0, y=0)

    fenetre.after(600000, lambda: fenetre.destroy())
    fenetre.mainloop()

    lcd.clear()

#RUN_FUNCTION_WITH_TIMING

schedule.every(3).seconds.do(update_weather)

while 1:
    schedule.run_pending()
