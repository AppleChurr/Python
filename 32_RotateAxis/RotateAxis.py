import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


# 회전 행렬 생성 함수
def rotation_matrix(roll, pitch, yaw):
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(roll), -np.sin(roll)],
                    [0, np.sin(roll), np.cos(roll)]])
    
    R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                    [0, 1, 0],
                    [-np.sin(pitch), 0, np.cos(pitch)]])
    
    R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                    [np.sin(yaw), np.cos(yaw), 0],
                    [0, 0, 1]])
    
    R = np.dot(R_z, np.dot(R_y, R_x))
    return R

def draw_cube(ax, vertices):
    edges = [
        [vertices[0], vertices[1]],
        [vertices[0], vertices[2]],
        [vertices[0], vertices[3]],
    ]

    if hasattr(ax, 'cube_lines'):
        for line in ax.cube_lines:
            line.remove()

    colors = ['red', 'green', 'blue']

    ax.cube_lines = []
    i = 0
    for edge in edges:
        line, = ax.plot(*zip(*edge), color=colors[i])
        i += 1
        ax.cube_lines.append(line)




# 애니메이션 업데이트 함수
def update(frame):

    ax.clear()

    draw_cube(ax, rotated_vertices[frame])

    xList.append(rotated_vertices[frame][1])
    yList.append(rotated_vertices[frame][2])
    zList.append(rotated_vertices[frame][3])

    if len(xList) >= 40:
        xList.pop(0)
        yList.pop(0)
        zList.pop(0)

    for axAxis, data, cc in zip([axX, axY, axZ], [xList, yList, zList], ['r', 'g', 'b']):
        x, y, z = zip(*data)

        xlimit = axAxis.get_xlim() + x
        ylimit = axAxis.get_ylim() + y
        zlimit = axAxis.get_zlim() + z

        axAxis.clear()
        axAxis.plot(x, y, z, c=cc, linestyle='--', linewidth=1)
        axAxis.scatter(x[-1], y[-1], z[-1], c=cc, marker='o')

        axAxis.set_xlim(min(xlimit), max(xlimit))
        axAxis.set_ylim(min(ylimit), max(ylimit))
        axAxis.set_zlim(min(zlimit), max(zlimit))




# CSV 파일 읽기
df = pd.read_csv('gyro.csv', header=None, names=['Euler_Roll', 'Euler_Yaw', 'Euler_Pitch',\
                                                    'Accelerometer_X', 'Accelerometer_Y', 'Accelerometer_Z',\
                                                    'OffsetEuler_Roll', 'OffsetEuler_Pitch', 'OffsetEuler_Yaw',\
                                                    'Rotation_Roll', 'Rotation_Pitch', 'Rotation_Yaw', \
                                                    'Date', 'Time'])

# 직육면체의 원래 꼭짓점 정의
vertices = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
])


xList = []
yList = []
zList = []
rotated_vertices = []

for frame in range(len(df)):
    roll = np.radians(df['Euler_Roll'].iloc[frame])
    pitch = np.radians(df['Euler_Pitch'].iloc[frame])
    yaw = np.radians(df['Euler_Yaw'].iloc[frame])

    R = rotation_matrix(roll, pitch, yaw)
    rotated_vertices.append(np.dot(vertices, R.T))

all_x, all_y, all_z = zip(*[coord for data in rotated_vertices for coord in data])

# 그래프 초기화 및 애니메이션 설정
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
axX = fig.add_subplot(322, projection='3d')
axY = fig.add_subplot(324, projection='3d')
axZ = fig.add_subplot(326, projection='3d')

ax.set_xlim(min(all_x), max(all_x))
ax.set_ylim(min(all_y), max(all_y))
ax.set_zlim(min(all_z), max(all_z))

axX.set_xlim(rotated_vertices[0][1][0] - 0.0001, rotated_vertices[0][1][0] + 0.0001)
axX.set_ylim(rotated_vertices[0][1][1] - 0.0001, rotated_vertices[0][1][1] + 0.0001)
axX.set_zlim(rotated_vertices[0][1][2] - 0.0001, rotated_vertices[0][1][2] + 0.0001)

axY.set_xlim(rotated_vertices[0][2][0] - 0.0001, rotated_vertices[0][2][0] + 0.0001)
axY.set_ylim(rotated_vertices[0][2][1] - 0.0001, rotated_vertices[0][2][1] + 0.0001)
axY.set_zlim(rotated_vertices[0][2][2] - 0.0001, rotated_vertices[0][2][2] + 0.0001)

axZ.set_xlim(rotated_vertices[0][3][0] - 0.0001, rotated_vertices[0][3][0] + 0.0001)
axZ.set_ylim(rotated_vertices[0][3][1] - 0.0001, rotated_vertices[0][3][1] + 0.0001)
axZ.set_zlim(rotated_vertices[0][3][2] - 0.0001, rotated_vertices[0][3][2] + 0.0001)

# ani = FuncAnimation(fig, update, frames=range(0, len(df), 100), interval=5)
ani = FuncAnimation(fig, update, frames=len(df), interval=5)
plt.show()