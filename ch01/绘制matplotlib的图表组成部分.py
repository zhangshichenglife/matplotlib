import numpy as np
import matplotlib.pyplot as plt

# 1.2 准备数据
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# 1.3 绘制matplotlib 图表组成元素的函数用法

# 1.3.1 函数plot()  展示变量的趋势变化
# plt.plot(x, y, linestyle="-", linewidth=2, label="plot figure")
# x: x轴上的数值； y: y轴上的数值
# linestyle: 折线图线条风格 linewidth: 线条宽度
# label: 标记图形内容的标签文本
x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
plt.plot(x, y, linestyle='-', linewidth=2, label='plot figure')
plt.legend()
plt.show()

# 1.3.2 函数scatter()  寻找变量的关系
# plt.scatter(x, y, color="b", label="scatter figure")
# color: 散点图中的点的颜色 edgecolors: 点的外圈颜色
# xlim: 设置x轴数值显示范围 ylim: 设置y轴数值显示范围
# xlabel: 设置x轴的标签 ylabel: 设置y轴的标签
x = np.linspace(0.5, 10, 1000)
y = np.random.rand(1000)  # rand 均匀0-1分布
plt.scatter(x, y,
            color='red', edgecolors='green',
            label='scatter figure',
            )
plt.xlim(0, 10)
plt.ylim(0, 1)
plt.xlabel('x-aix')
plt.ylabel('y-aix')

plt.legend()
plt.show()


