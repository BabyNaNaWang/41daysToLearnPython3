# date:2019-4-20
# author:Ivo Wang
# describition:for循环、range函数、while循环、break语句
# editor for code: vs code

# for循环
# for循环指一种用来遍历可迭代对象的循环，这个过程称为遍历
# 语法：
# for [变量名] in [可迭代对象名]:
#    [指令]

# 循环遍历一个字符串:

name = 'Ivo'
for temp in name:
    print(temp)

# 遍历一个列表：

name_list = ['小明','小红','小李']
for temp in name_list:
    print(temp)

# 遍历一个元组

new_name_list = ('h','e','l')
for temp in new_name_list:
    print(temp)

# 遍历一个字典

name_dir = {1:1.1,2:2.1,3:3.1}
for temp in name_dir:
    print(temp)

# 可通过循环的方式改变可迭代对象中的元素

word_list = ['hello','python']
i = 0
for temp in word_list:
    target = word_list[i]
    target = target.upper()
    word_list[i] = target
    i += 1
print(word_list)

# 也可以使用enumerate函数去遍历该函数返回的结果

word_list = ['hello','python']
for i, show in enumerate(word_list):
    target = word_list[i]
    target = target.upper()
    word_list[i] = target
print(word_list)

# enumerate 函数
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为
# 一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

word_list = ['hello','python']
print(list(enumerate(word_list)))

word_list = ['hello','python']
for i , temp in enumerate(word_list):
    print(i,temp)

# 可以通过遍历多个列表，将遍历结果放入一个新列表

a = ['1','2','3','4']
b = ['5','6','7','8']
c = []
for temp in a:
    c.append(temp)
for temp in b:
    c.append(temp)
print(c)

# range 函数
# range函数创建一个整数序列通过
# range函数接受两个参数：序列起始数字和序列结束数字，
# 返回包含第一个参数到第二个参数之间（不含）的所有整数
# 如：

for i in range(1,4):
    print(i)

# while 循环
# 定义：一种只要表达式为True就一直执行的循环
# 语法：while [表达式]：[执行代码]
# 如3s倒计时代码:

x = 3
while x > 0:
    print('{}'.format(x))
    x -= 1
print('action')

# 如果条件表达式永远为True，则循环不会停止
# 不会停止的循环也叫死循环
# 如：

while True:
    print('hello world')

# break 语句
# break语句用来终止循环
# 如：
while True:
    print('hello world')
    break

# 应用：如输入'Q'退出程序

question = ['What is your favorite color?'
,'May I have your name?',
'May I have your wechat?']
i = 0
while True:
    print('输入Q退出：')
    a = input(question[i])
    if a == 'q':
        break
    i = (i + 1) % 3