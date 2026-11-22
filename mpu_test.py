from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

while True:
    accel = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()
    print(f"Akcel  X={accel['x']:.2f}  Y={accel['y']:.2f}  Z={accel['z']:.2f}")
    print(f"Zyro   X={gyro['x']:.2f}  Y={gyro['y']:.2f}  Z={gyro['z']:.2f}")
    print("----------------")
    time.sleep(0.5)