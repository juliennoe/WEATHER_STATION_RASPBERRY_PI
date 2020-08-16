from lcdmtrx import LcdMatrix

PORT_SERIE = '/dev/ttyACM0'
lcd = LcdMatrix(PORT_SERIE)
LCD_COLS = 16
LCD_ROWS = 2

lcd.clear_screen()
print('clear_screen')

