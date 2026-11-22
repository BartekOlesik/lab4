import board
import adafruit_vl53l0x
import time

sensor = adafruit_vl53l0x.VL53L0X(board.I2C())

while True:
    d = sensor.range
    if d > 500:
        print(d, "mm  DALEKO")
    elif d >= 200:
        print(d, "mm  BLISKO")
    else:
        print(d, "mm  ALARM")
    time.sleep(0.2)