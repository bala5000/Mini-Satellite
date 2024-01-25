import machine
import utime

MQ2 = machine.ADC(26)

while True:
    smoke_value = MQ2.read_u16()
    voltage = MQ2.read_u16()*0.000056
    
    print("Smoke_value is:", smoke_value)
    print("Voltage is:",voltage)
    
    utime.sleep(4)