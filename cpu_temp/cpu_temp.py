import I2C_LCD_driver
import time
from  ram_usage import *
mylcd = I2C_LCD_driver.lcd()

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = file.read()
        return float(temp) / 1000.0

while True:
    mylcd.lcd_display_string("Cpu Temp: %s" %get_cpu_temperature(),1)
    
    mylcd.lcd_display_string("Ram : %s / %s" %get_memory_usage(), 2)
    time.sleep(3.0)
