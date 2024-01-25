import machine
import utime
from chittiSat.sdcard import *
import uos
from chittiSat.pressure import *
from chittiSat.assistant import *

i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0))

devices = i2c.scan()

if devices:
    print(devices)

bmp280 = BMP280(i2c)

calibrate.pressure(bmp280)

spi = machine.SPI(1, sck=machine.Pin(14), mosi=machine.Pin(15), miso=machine.Pin(12))

sd = SDCard(spi)

uos.mount(sd, '/sd')
print("sdcard connected")
print(uos.listdir('/sd'))

file_list = uos.listdir('/sd')
myfile = file_list[0]  # Assuming you want the first file in the directory

with open(myfile, "w") as f:
    f.write("Time")
    f.write(",")
    f.write("Pressure")
    f.write("\n")

while True:
    Pressure = bmp280.pressure
    t = utime.ticks_ms() / 1000

    with open(myfile, "a") as f:  # Use "a" to append to the existing file
        f.write(str(t))
        f.write(",")
        f.write(str(Pressure))
        f.write("\n")
        f.flush()

    print("Value saved")

    utime.sleep(10)