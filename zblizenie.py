import board
import adafruit_vl53l0x
import time

sensor = adafruit_vl53l0x.VL53L0X(board.I2C())

while True:
    d = sensor.range
    if d < 100:
        print(d, "mm  UWAGA - obiekt bardzo blisko!")
    elif d < 300:
        print(d, "mm  Obiekt blisko")
    else:
        print(d, "mm  Brak obiektu w poblizu")
    time.sleep(0.2)