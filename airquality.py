from machine import Pin
from chittiSat.mq2 import MQ2
import utime
from chittiSat.assistant import dashboard

led = Pin(25,Pin.OUT)
sensor =MQ2(pinData = 26)

sensor.calibrate()

while True:
    GAS = sensor.readLPG()
    Smoke = sensor.readSmoke()
    Methane = sensor.readMethane()
    Hydrogen = sensor.readHydrogen()
    
    dashboard.sendAir(Smoke, GAS, Methane, Hydrogen)
    
    if GAS>10:
        print("Gas Detected")
        led.on()
        
    else:
        print("No Gas Detected")
        led.off()
        
    utime.sleep(0.5)
    