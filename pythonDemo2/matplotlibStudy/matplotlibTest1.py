import pandas
import matplotlib.pyplot as plt
from numpy import arange
import numpy


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# pandas读文件
score = pandas.read_csv('E:/LyyPycharmFile/2015score.csv'
                        ,encoding='GBK')
pandas.set_option('display.max_columns',100)
print(score)
print("============================================================")


# plt.plot()
# plt.show()

#
# plt.plot(score["学号"],score["仓储配送"])
# plt.show()
#
# # 为了让横坐标的数值更方便观看，设置横坐标名称的倾斜角度
# plt.plot(score["学号"],score["仓储配送"])
# plt.xticks(rotation=90)
# plt.show()


# # 表名横坐标，纵坐标的含义   以及标题
# plt.plot(score["学号"],score["仓储配送"])
# font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
# plt.xticks(rotation=45)
# plt.xlabel("number",font)
# plt.ylabel("score",font)
# plt.title("relationship between number and score",font)
# plt.show()

#
#
# # 操作子图   显示两行两列的矩阵图中的1,3,4个
# fig = plt.figure()
# ax1 = fig.add_subplot(2,2,1)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)
# plt.show()
#
# #
# # 显示一个空白的图
# fig1 = plt.figure()
# plt.show()
#
#
# # 显示条形图   .plot
# #  figsize 设置图形的长度和宽度
# fig2 = plt.figure(figsize=(3,3))
# # 设置子图  记住是在原有图形的基础上面添加子图
# ax3 = fig2.add_subplot(2,1,1)
# ax4 = fig2.add_subplot(2,1,2)
#
# # 设置子图的数据  plot设置数据
# ax3.plot(numpy.random.randint(1,5,5),numpy.arange(5))
# ax4.plot(numpy.arange(10)*3,numpy.arange(10))
# plt.show()


#
# # 在一个图形中显示两条线
# data1 = score["仓储配送"]
# data2 = score["体育"]
#
# fig = plt.figure(figsize=(10,6))
#
# plt.plot(score["学号"],data1,c = "red")
# plt.xticks(rotation = 45)
# plt.plot(score["学号"],data2,c = "blue")
# plt.show()


# fig = plt.figure(figsize=(10,6))
# colors = ['red','blue','green','orange','black']
# for i in range(5):
#     start_index = i*12
#     end_index = (i+1)*12
#     subset = score[start_index:end_index]
#     # 设置label
#     label1 = str(1+i)
#     plt.plot(subset["学号"],subset["体育"],c = colors[i],label = label1)
# # 自己去选择label的最佳位置
# plt.legend(loc = 'best')
# print(help(plt.legend))
# plt.xlabel("number")
# plt.ylabel("score")
# plt.title("relationship between number and score")
# plt.show()



# 画条形图   .bar
cols = ["姓名","仓储配送","经济学","体育","铁路车辆设备运用","铁路站场设备运用"]
norm_score = score[cols]
print(norm_score)
print('---------------------------------------------------------------')
score_cols = ["仓储配送","经济学","体育","铁路车辆设备运用","铁路站场设备运用"]
# # 第一个学生各科的成绩
# bar_height = norm_score.ix[0,score_cols].values
# # 在1到5 的位置显示x坐标值
# tick_position = range(1,6)
# # 设置每个柱之间的距离，
# # 第一个柱离0之间的距离是0.9，
# # 后面每个柱之间相隔1
# bar_position = arange(5)+0.9
# fig, ax = plt.subplots()
# # 柱的位置  柱的高度   柱的宽度
# ax.bar(bar_position,bar_height,0.3)
# # 在指定的地方显示x的坐标值
# ax.set_xticks(tick_position)
# plt.xlabel("each course")
# plt.ylabel("score")
# plt.title("bar of score")
# # 设置x坐标下的名称  名称展示的角度
# ax.set_xticklabels(score_cols,rotation = 45)
# plt.show()
#
# # 横纵坐标调换位置
# # ax.barh(bar_position,bar_height,0.5)




#
# # 散点图  .scatter
# fig,ax = plt.subplots()
# ax.scatter(score["仓储配送"],score["经济学"])
# plt.show()
# #
#
#
# # 直方图画法  .hist
# fig,ax = plt.subplots()
# # ax.hist(norm_score["仓储配送"])
# # bin 出现的条数
# # range 取值范围 比如这里取的60-100的分数，显示不同区间分数的个数
# ax.hist(norm_score["仓储配送"],range = (60,100),bins=10)
# plt.show()
#
#
# # 画带子图的直方图
# fig = plt.figure(figsize=(5,20))
# ax1 = fig.add_subplot(4,1,1)
# ax2 = fig.add_subplot(4,1,2)
# ax3 = fig.add_subplot(4,1,3)
# ax4 = fig.add_subplot(4,1,4)
# # range  设置x轴显示的区间
# ax1.hist(score["仓储配送"],range = (50,100),bins = 5)
# # set_ylim 设置y轴显示的区间
# ax1.set_ylim(0,20)
# plt.show()


# 盒图  boxplot
fig,ax = plt.subplots()
ax.boxplot(score["仓储配送"])
ax.set_xticklabels(["课程成绩"])
plt.show()

# 一个大图中显示四个盒图  创建一个子图直接 subplots
fig,ax = plt.subplots()
# 显示所有的成绩  这里的参数去所有的成绩
ax.boxplot(score[score_cols].values)
# 设置x轴显示的名字 旋转角度
ax.set_xticklabels(score_cols,rotation = 90)
# 设置y轴显示的区间
# ax.set_ylim(0,5)
plt.show()













