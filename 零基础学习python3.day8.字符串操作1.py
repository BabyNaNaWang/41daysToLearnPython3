# date:2019-4-18
# author:Ivo Wang
# describition:三引号字符串、索引、字符串是不可变的、字符串拼接、改变大小写、字符串乘法、格式化、分割
# editor for code: vs code

# 三引号字符串
# 如果字符串需要跨一行以上，可以使用三引号

my_str = '''第一行
第二行
第三行'''
print(my_str)

# 字符串索引
# 字符串第一个索引的值为0，其后每个索引低增1

'''my_str = 'hello world'
print(my_str[0])
print(my_str[1])
print(my_str[2])

# 查找字符串索引的值大于最后一个索引的值，报错：IndexError

# my_str = 'he'
# print(my_str[2])

# 负索引：从右想左查找可迭代对象中元素的索引(必须为负数)

my_str = 'he'
print(my_str[-1])

# 字符串是不可改变的
# 字符串和元组一样是不可改变的，无法修改字符串中的字符
my_str = 'he'
my_str = 'she' # 创建新字符串

# 字符串拼接：+
# 可使用加法操作符，将两个字符串拼接在一起，组成一个新的字符串

a = 'he'
b = 'll'
c = 'o'
print(a + b + c)

# 字符串乘法：

a = 'hello'
print(a * 3)

# 字符串大小写
# 大写：upper

a = 'hello world'
print(a.upper())

# 或者

print('hello world'.upper())

# 小写:lower

a = 'HELLO WORLD'
print(a.lower())

# 或者

print('HELLO WORLD'.lower())

# 首字母大写:capitalize

a = 'hello world'
print(a.capitalize())

# 或者

print('hello world'.capitalize())

# 格式化
# 可使用format方法创建新字符串
# 该方法会把字符串中的{}替换成传入的字符串

a = 'Ivo{}'.format('wang')
print(a)

# 也可以把变量作为参数

last_name = 'wang'
print('Ivo{}'.format(last_name))

# 也可以使用多个大括号

name = 'Ivo Wang'
birthday = '1900.01.01'
print('{}的生日是{}'.format(name,birthday))

# 应用：将一个用户键盘输入的信息创建成一个字符串打印

name = input('请输入你的姓名：')
age = input('请输入年龄：')
hometown = input('请输入家乡：')'''
'''print('''
'''大家好，
我叫{}，
来自{},
今年{}岁'''
'''.format(name,hometown,age))'''

# 输入王二小、山东、18后打印结果

# 分割
# 可通过split方法将字符串分割为两个及以上字符串
# 需要在方法中传入一个字符串作为分割参数

a = 'hello'
print(a.split('e'))

# 作用
# 将一段英语分割成一个一个单词。

a = 'Your happy passer-by all knows'
b = a.split(' ')
for temp in b:
    print(temp)