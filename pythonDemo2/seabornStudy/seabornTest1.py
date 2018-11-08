import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def sinplot(fip =1):
    # 在0到14之间取100个值
    x = np.linspace(0,14,100)
    # i取1到6的值
    for i in range(1,7):
#        print(i)
        plt.plot(x,np.sin(x+i*0.5)*(7-i)*fip)

# # sns.set使用seaborn默认的参数
# #sns.set()
# # seaborn默认有5种风格 通过set_style设置
# # dark white ticks  whitegrid  darkgrid
# sns.set_style("whitegrid")
# # 去掉上面和右边的线
# sinplot()
# # 去掉左右底部的线
# sns.despine(left=True,right=True,bottom=True)
# # plt.show()
#
#
# # 使用with来指定某些子图的风格
# with sns.axes_style("darkgrid"):
#     plt.subplot(211)
#     sinplot()
# plt.subplot(212)
# sinplot(-1)
# plt.show()


# sns.set_context("paper")
# plt.figure(figsize=(8,6))
# sinplot()
# plt.show()



# sns.set_context("talk")
# plt.figure(figsize=(8,6))
# sinplot()
# plt.show()


# sns.set_context("poster")
# plt.figure(figsize=(8,6))
# sinplot()
# plt.show()


# # font-scale 字体大小   lines.width 线条宽度
# sns.set_context("notebook",font_scale=1,rc={"lines.linewidth":2.5})
# sinplot()
# plt.show()



# sns.set_style("whitegrid")
# # np.random.normal 生成高斯分布随机数
# data = np.random.normal(size=(20,6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# # plt.show()

sinplot()
sns.set(rc={"figure.figsize":(6,6)})
plt.show()


# 调色板 color_palette  set_palette
current_palette = sns.color_palette()
sns.palplot(current_palette)
plt.show()


















