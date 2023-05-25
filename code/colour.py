from machine import Pin,I2C # возможность работать с I2C ротоколом
from neopixel import NeoPixel # работа с адресными светодиодами
from MX1508 import * # драйверы двигателя
from VL53L0X import * # работа с лазерным дальномером
from tcs import * # работа с датчиком цвета
from time import sleep_ms,sleep # задержки в мс и с
import uasyncio as asio # возможность асинхронн программирования
import aioespnow # асинхронный ESP-now
import network # функции работы по wi-fi

i2c_bus = I2C(0, sda=Pin(16), scl=Pin(17)) # создание шины под датчик цвета
tcs = TCS34725(i2c_bus)
tcs.gain(4)#gain must be 1, 4, 16 or 60 (значение усиления)
tcs.integration_time(80) # время накопления данных и решения по цвету
color=['Red','Yellow','White','Green','Black','Cyan','Blue','Magenta'] # набор обрабатываемых цветов
alfa=0.8 # параметр для фильтра сглаживания дистанции
debug=1 # выводится ли отладочная информация

R_W_count,W_count,col_id,col_id_l,direct,di,dist,busy,busy_col,col_sel=0,0,0,0,0,0,500,0,0,5 # инициализация глобальных переменных

def color_det():
    global col_id,col_id_l
    while 1:
        rgb=tcs.read(1)
        r,g,b=rgb[0],rgb[1],rgb[2]
        h,s,v=rgb_to_hsv(r,g,b)
        if 0<h<60: # определение цвета
            col_id_l=col_id
            col_id=0
        elif 61<h<120:
            col_id_l=col_id
            col_id=1
        elif 121<h<180:
            if v>100:
                col_id_l=col_id
                col_id=2
            elif 25<v<100:
                col_id_l=col_id
                col_id=3
            elif v<25:
                col_id_l=col_id
                col_id=4
        elif 181<h<240:
            if v>40:
                col_id_l=col_id
                col_id=5
            else:
                col_id_l=col_id
                col_id=6
        elif 241<h<360:
            col_id_l=col_id
            col_id=7
        #sleep(1)
        if debug:
            print('Color is {}. R:{} G:{} B:{} H:{:.0f} S:{:.0f} V:{:.0f}'.format(color[col_id],r,g,b,h,s,v))      

color_det()