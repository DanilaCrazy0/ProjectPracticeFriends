from machine import Pin,I2C # возможность работать с I2C ротоколом
from neopixel import NeoPixel # работа с адресными светодиодами
from MX1508 import * # драйверы двигателя
from VL53L0X import * # работа с лазерным дальномером
from tcs import * # работа с датчиком цвета
from time import sleep_ms,sleep # задержки в мс и с
import uasyncio as asio # возможность асинхронн программирования
import aioespnow # асинхронный ESP-now
import network # функции работы по wi-fi

sp = 1023
sp_mas = [1023, 512]

motor_R = MX1508(2, 4)
motor_Д = MX1508(17, 18)
print('ping pin')
sleep(2)
motor_R.forward(1023)
motor_L.forward(1023)
print('ping run forward 1023')
sleep(2)
motor_R.reverse(512)
motor_L.reverse(512)
print('ping run reverse 512')
sleep(2)
motor_R.forward(0)
motor_L.forward(0)
print('ping run stop')