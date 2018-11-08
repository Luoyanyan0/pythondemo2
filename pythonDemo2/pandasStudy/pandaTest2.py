from pandas import Series
import pandas
import numpy

content = pandas.read_csv('E:/LyyPycharmFile/test1.csv',
                          encoding = 'GB2312')
serial_math = content['数学分数']
print(serial_math)
print('---------------------------------------------')
serial_english = content['英语分数']
print(serial_english)
print('---------------------------------------------')
serial_name = content['姓名']
print(serial_name)
print('---------------------------------------------')
print('=======================================================')



# Series 输出两列之间的对应关系
# 用一列为index，找到对应列的值
# series 可以使用数字当索引 也可以使用string当索引
math_val = serial_math.values
name_val = serial_name.values
serial_new = Series(math_val, index = name_val)
print(serial_new[['A红红','I花花']])
print('=======================================================')


# 设置了用name当索引之后，
# 仍然可以用数字当索引来获取series的内容
new_print = serial_new[1:5]
print(new_print)
print('=======================================================')


# 上面是按照姓名获得成绩 但是姓名的排序是没有规则的
# 现在将index即姓名进行排序再取分数值
# 获得serial_new的旧的index，将其放入list中
oriindex= serial_new.index.tolist()
print(oriindex)
print('---------------------------------------------')
# 将旧的list进行排序
new_index = sorted(oriindex)
print(new_index)
print('---------------------------------------------')
# 利用排好序的index  reindex Series中的值
sort_by_index = serial_new.reindex(new_index)
print(sort_by_index)
print('=======================================================')


# 上面操作的简单实现  sort_index  sort_value
print(serial_new.sort_index()[0:5])
print('---------------------------------------------')
print(serial_new.sort_values()[0:5])
print('=======================================================')


# numpy 和series的混合操作
print(numpy.add(serial_new,serial_new))
print('---------------------------------------------')
print(numpy.sin(serial_new))
print('---------------------------------------------')
print(numpy.max(serial_new))
print('=======================================================')



# 运算
print(serial_new[(serial_new > 10) & (serial_new < 80)])
print('---------------------------------------------')
# 注意这里的两个参数，都必须取到value值
serial_new2 = Series(serial_english.values,
                     index = serial_name.values)
print((serial_new + serial_new2)/2)






