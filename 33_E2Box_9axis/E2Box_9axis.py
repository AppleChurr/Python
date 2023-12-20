import serial
import matplotlib.pyplot as plt
import numpy as np

serial_port = 'COM10'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate, timeout=0.1)

# 초기화: 데이터를 저장할 리스트 생성
roll_data = []
pitch_data = []
yaw_data = []
x_accel_data = []
y_accel_data = []
z_accel_data = []

# 그래프 초기화
fig = plt.figure()

# 각각의 subplot 정의
axsRoll = fig.add_subplot(321)
axsPitch = fig.add_subplot(323)
axsYaw = fig.add_subplot(325)
axsXacc = fig.add_subplot(322)
axsYacc = fig.add_subplot(324)
axsZacc = fig.add_subplot(326)

axs = [axsRoll, axsPitch, axsYaw, axsXacc, axsYacc, axsZacc]
datas = [roll_data, pitch_data, yaw_data, x_accel_data, y_accel_data, z_accel_data]
titles = ['Roll', 'Pitch', 'Yaw', 'X Acceleration', 'Y Acceleration', 'Z Acceleration']
colors = ['r', 'g', 'b', 'r', 'g', 'b']

tick = 0
maxframe = 40

def update_plot():

    for ax, data, title, cc in zip(axs, datas, titles, colors):
        ax.clear()
        ax.plot(data, c=cc, label=title)
        ax.set_title(title)
        ax.set_xlim(tick, maxframe + tick)

    for ax in axsRoll, axsPitch, axsYaw:
        ax.axhline(y=-np.pi, color='black', linestyle='--')
        ax.axhline(y=0, color='black', linestyle='--')
        ax.axhline(y=np.pi, color='black', linestyle='--')

        ax.set_ylim(-np.radians(200), np.radians(200))

    for ax in axsXacc, axsYacc, axsZacc:
        ax.set_ylim(-35, 35)

    plt.pause(0.0000001)

try:
    while True:
        lines = ser.read(ser.in_waiting).decode('utf-8').splitlines()

        if lines:
            line = lines[-1]
            data = line.split(',')

            if len(data) < 6:
                continue
            
            roll = np.radians(float(data[0][1:]))  # '*' 문자 제거 후 float로 변환
            pitch = np.radians(float(data[1]))
            yaw = np.radians(float(data[2]))
            x_accel = float(data[3])
            y_accel = float(data[4])
            z_accel = float(data[5][:-1])  # 마지막 문자인 개행 문자 제거 후 float로 변환

            sensor_data = [roll, pitch, yaw, x_accel, y_accel, z_accel]

            for ldata, data in zip(datas, sensor_data):
                ldata.append(data)
                if len(ldata) > maxframe :
                    ldata.pop(0)
                    
            update_plot()
            

except KeyboardInterrupt:
    ser.close()
    print("프로그램이 종료되었습니다.")
