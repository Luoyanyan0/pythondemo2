import numpy

txt_content = numpy.genfromtxt("E:/LyyPycharmFile/test.txt",delimiter=",",dtype=str)
print(type(txt_content))
print(txt_content)
#print(help(numpy))


array = numpy.array([1,2,3,4,5,6])
print(array)

#matrix = numpy.array([1,2],[3,4],[5,6])
# 报错  ValueError: only 2 non-keyword arguments accepted
matrix = numpy.array([[1,2],[3,4],[5,6]])
print(matrix)






