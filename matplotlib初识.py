import matplotlib.pyplot as plt
import numpy as np


# 设置画板
fig = plt.figure()
# 设置轴
ax = fig.add_subplot(111) # 111 指的是 画板共1行1列， 在第一个位置作图
ax.set(xlim=[0.5, 4.5],
       ylim=[-2, 8],
       xlabel='X-Axis',
       ylabel='Y-Axis',
       title='An Example Axes')
plt.show()

# 一个画板存放多个图形
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
plt.show()

# 批量生成坐标轴和 title
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set(title='Upper Left')
axes[0, 1].set(title='Upper Right')
axes[1, 0].set(title='Lower Left')
axes[1, 1].set(title='Lower Right')
plt.show()

# 基本绘图
# 数据准备
x = np.linspace(0, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

ax1.plot(x, y_sin)
ax2.plot(x, y_sin, 'go--', linewidth=1, markersize=2)


fig.show()