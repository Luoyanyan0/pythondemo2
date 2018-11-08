import pandas
import numpy

content = pandas.read_csv('E:/LyyPycharmFile/test1.csv',encoding = 'GB2312')
print(content)
print('----------------------------------')
print(type(content))
print('----------------------------------')
print(content.dtypes)
print('---------------------')
# 不加参数 默认显示前面的5行数据
print(content.head())
print('----------------------------------')
# 加参数 显示前面的三行数据
print(content.head(3))
print('----------------------------------')
# 显示最后几行的数据
print(content.tail())
print('----------------------------------')
# 返回列名
print(content.columns)
print('----------------------------------')
# 返回文件规格
print(content.shape)
print('===================================')



# 获取文件指定位置的信息  按行获取
# 获取第一行的数据
# 注意下标是用中括号括起来的  并且下标是不允许越界的
print(content.loc[0])
print('----------------------------------')
# 展示4,5,6,7 行内容
# 注意：这里的数据包括最后一个下标的数据
print(content.loc[3:6])
print('----------------------------------')
# 展示第2,5,7 行内容
# 注意：选择指定不连续三行以上的时候，loc中的数据需要用[]括起来
print(content.loc[[1,4,6]])
print('===================================')


# 按列获取内容
# 获取 学号 列的所有信息 直接文件名['列名']
print(content['学号'])
print('----------------------------------')
# 获取指定多列的内容 需要将多列的列名添加进一个[]中
print(content[['姓名','语文分数']])
print('----------------------------------')
print('===================================')


# 根据名称分数，获取所有科目的分数
# 首先将所有的列名放入一个list中
scores = content.columns.tolist()
print(scores)
print('----------------------------------')
# 创建一个list 用来接收所有的分数   endswith
score = []
for c in scores:
    if c.endswith('分数'):
        # 将所有包含分数的列名取出来放到一个list中去
        score.append(c)
print(score)
print('----------------------------------')
# 打印文件中所有以分数结尾的列
print(content[score])
print('===================================')



# pandas运算
print(content['数学分数']/100)
print('===================================')


# pandas排序  文件名.sort_values()
# inplace 为true代表用新排序的数据代替原来的数据
content.sort_values('数学分数',inplace = True)
print(content['数学分数'])
print('----------------------------------')
print(content)
print('----------------------------------')
content.sort_values('数学分数',inplace = True, ascending = False)
print(content['数学分数'])
print('----------------------------------')
print(content)
print('===================================')


# pandas 操作表格中的空值
# 先取出所有的语文分数   分数为空的那里会显示NaN
chinese = content['语文分数']
print(chinese)
print('----------------------------------')
# 用pandas.isnull判断chinese中是否为空
# 空的显示true  非空显示false
chinese_is_null = pandas.isnull(chinese)
print(chinese_is_null)
print('----------------------------------')
# chinese包含所有语文分数
# chinese_is_null 若分数为空显示true
# 两者组合展示语文分数中成绩为空的那行
chinese_null_true = chinese[chinese_is_null]
print(chinese_null_true)
print('----------------------------------')
# len计算长度
print(len(chinese_null_true))
print('===================================')


# 计算语文分数的平均值
# 法一  语文分数的和/语文分数总列数  （没有去掉值为空的行）
# 这个方法不行  没有去掉空行 显示nan
ave1 = sum(content['语文分数']) / len(content['语文分数'])
print(ave1)
# ave1 = content['语文分数'].sum() / content['语文分数'].size  这个可以哎
print('----------------------------------')


# 法二 去掉空行
good_scores = content['语文分数'][chinese_is_null == False]
ave2 = sum(good_scores) / len(good_scores)
print(ave2)
print('----------------------------------')


# 法三  利用pandas函数 mean
ave3 = content['语文分数'].mean()
print(ave3)
print('===================================')


# 分别求1,2,3班语文的平均成绩
# 班级有三种 分别是1,2,3班
classes = [1,2,3]
# 存放班级 平均成绩  键值对
score_by_class = {}
# 遍历班级，找到每个班级对应的所有行
for this_class in classes:
    # 找到班级对应的所有行
    rows = content[content['班级'] == this_class]
    print(rows)
    print('----------------------------------')
    # 找到每个班级对应的所有行的语文分数
    chinese_score = rows['语文分数']
    print(chinese_score)
    print('----------------------------------')
    # 求语文分数的平均数
    chinese_ave = chinese_score.mean();
    print(chinese_ave)
    print('----------------------------------')
    # 将键值对放入字典当中
    score_by_class[this_class] = chinese_ave
    print(score_by_class)
    print('----------------------------------')
print(score_by_class)
print('===================================')



# 判断语文成绩几个与班级之间的关系 pivot_table
# aggfunc = numpy.mean 不写的话默认也是这种方式
chinese_is_fail = content.pivot_table(index = '班级',
                                      values = '语文分数',
                                      aggfunc = numpy.mean)
print(chinese_is_fail)
print('===================================')



# 查看班级与数学成绩之间的关系
math_is_fail = content.pivot_table(index='班级', values='数学分数')
print(math_is_fail)
print('===================================')


# 班级与语数外总分数的关系
sum_score = content.pivot_table(index='班级',
                                values=['语文分数','数学分数','英语分数'],
                                aggfunc=numpy.sum)
print(sum_score)
print('===================================')



# dropna 去掉缺失值的某行或列
# 去掉有缺失值的所有列
# dropna_column = content.dropna(axis=1)
# print(dropna_column)
print('----------------------------------')
dropna_row = content.dropna(axis=0,subset=['语文分数','班级'])
print(dropna_row)
print('===================================')


# 定位
# 显示第二行的姓名   数据从第0行算起
s_name = content.loc[2,'姓名']
print(s_name)
print('===================================')


# 排序
# 根据英语分数降序
sort_by_english = content.sort_values('英语分数',
                                      ascending=False)
print(sort_by_english)
print('----------------------------------')
#上面排序的index不规范，重新规范index
new_sort = content.sort_values('英语分数',
                               ascending=False).reset_index()
print(new_sort)
print('===================================')



# 定义一个函数取第6条数据
def hundredth_row(column):
# 注意这里是column.loc 不是content.loc 不然打印内容形式和文件一致
    row = column.loc[5]
    return row

Row = content.apply(hundredth_row)
print(Row)
print('===================================')


# 输出每一列各有多少缺失值
def col_is_null(col):
    cnull = pandas.isnull(col)
    null = col[cnull]
    print(null)
    return len(null)

col_null = content.apply(col_is_null)
print(col_null)
print('===================================')


# series dataframe的子结构
print(type(content))
print('----------------------------------')
serial_chinese = content["语文分数"]
print(type(serial_chinese))