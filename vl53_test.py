import board
import adafruit_vl53l0x
import time

sensor = adafruit_vl53l0x.VL53L0X(board.I2C())

while True:
    print("Odleglosc:", sensor.range, "mm")
    time.sleep(0.2)