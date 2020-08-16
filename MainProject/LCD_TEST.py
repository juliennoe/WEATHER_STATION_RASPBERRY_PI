from lcdbackpack import LcdBackpack
import time
 
lcd = LcdBackpack('/dev/ttyACM0', 115200)
lcd.connect()
lcd.clear()
lcd.set_brightness(255)
columns = 16
rows = 2
lcd.set_lcd_size(columns, rows)
lcd.write("pouet!\rprout\r")
time.sleep(1)
lcd.write("bob\rquick")
lcd.set_backlight_green()
time.sleep(1)
lcd.set_backlight_red()
time.sleep(1)
lcd.set_backlight_white()
lcd.set_autoscroll(True)
lcd.set_cursor_home()



