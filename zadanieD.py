from mpu6050 import mpu6050
import board
import adafruit_vl53l0x
import math
import time

mpu = mpu6050(0x68)
tof = adafruit_vl53l0x.VL53L0X(board.I2C())

PROG_RUCHU = 2.0   # m/s2 odchylki od g
PROG_ODL = 300     # mm

while True:
    a = mpu.get_accel_data()
    magnitude = math.sqrt(a["x"]**2 + a["y"]**2 + a["z"]**2)
    ruch = abs(magnitude - 9.81) > PROG_RUCHU
    d = tof.range

    stan = "ALARM" if (ruch and d < PROG_ODL) else "OK"
    print(f"{d:5d} mm | {magnitude:5.2f} m/s2 | ruch: {'TAK' if ruch else 'nie'} | {stan}")
    time.sleep(0.1)