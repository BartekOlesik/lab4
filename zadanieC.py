from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)
sensor.set_gyro_range(sensor.GYRO_RANGE_2000DEG)  # domyslnie max 250 deg/s

maks = {"x": 0.0, "y": 0.0, "z": 0.0}
print("Pomiar przez 10 s - obracaj czujnikiem...")
start = time.time()

while time.time() - start < 10:
    g = sensor.get_gyro_data()
    for axis in maks:
        maks[axis] = max(maks[axis], abs(g[axis]))  # abs: obrot w obie strony
    time.sleep(0.01)

print("Maksymalna predkosc obrotowa:")
for axis in "xyz":
    print(f"{axis.upper()}: {maks[axis]:.1f} deg/s")