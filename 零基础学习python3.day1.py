import math
# date:2019-4-10
# author：Ivo Wang
# describtion ： first demo

print('my first demo')


# date:2019-4-11
# author：Ivo wang
# describtion ： Introduction to programming

# 第三章编程概论
# 3.1 示例 
# 第一个程序：打印100次
# 通过字符串x100打印：
print('hello,world！'*100)
#通过for循环打印，此为换行
for i in range(100):
    print('hello,world')

#3.2 注释  注释代码编译器不会执行

#单行注释通过#创建，如：
# 这是一个单行注释

#多行注释以'''创建，以'''结尾，如：
'''这是第一行注释
   这是第二行注释'''

#注释的作用：对代码功能进行描述,如下：
# 计算对角线长度
l = 4
w = 10
d = math.sqrt(l**2+w**2)
print(d)

# 3.3 打印
# 通过内置函数print打印要输出的内容
# 打印字符串
print('python')
#打印变量
a = 'demo'
print(a)
#打印数字
print(3)
#打印字符串3
print('3')

#3.4 代码行
#作用：区别代码行数
#有时代码超过一行，可以用三引号、圆括号、方括号、或者大括号扩展至新一行，如：

print('''this is a really really
long line of code.''')

print\
('''this is a really really
long line of code.''')

#3.5 关键字
#python中具备特殊意义的字，即关键字，如for、in等

#3.6 间距
#以下面的代码为例,print相较于for缩进了4个空格符，如果不是4个空格符缩进，代码将会报错。
for i in range(100):
    print('hello,world')

#3.7 数据类型
# 概念：python将数据划分成不同的类型，即数据类型(data type)
# 每一个数据值，如 2 或者'hello world',被称为对象。
# 字符串：数据类型为str的对象，称其为字符串，字符串包括一个或者多个字符组成的序列
# 字符：类似a或者1这样的单个符号，以单引号和双引号表示
# 整型数据：整数(1,2,3,4等)的数据类型为整型数据(int,integer)
# 浮点数：小数的数据类型为float,2.1、8.2和999.99等都是类型为float的对象,称之为浮点数
# 布尔值：数据类型为bool的对象呗称谓布尔值(boolean)，仅有True和False两个值

#3.8 常量和变量
# 常量：一个永远不变的值，示例中每一个数字，都是常量
# 变量：指会改变的值,变量由一个或者多个字符组成的名称构成，并使用赋值符'='赋予这个名称一个值
# 变量之间可通过运算符进行算数运算，如：
x = 10 
y = 10
z = x + y
print(z)
a = x - y
print(a)

# 变量的增加或者缩小可将变量赋予给自身,如：
b = 10 
b = b + 1
print(b)
# 还可以写作
b = 10
b += 1
print(b)
# 缩小同上

# 需要注意的地方：
# 1、变量名称不允许出现空格。
# 2、变量名只能使用特定的字母、数字、下划线。
# 3、变量名不能以数字开头。
# 4、不能使用python关键字作为变量名。
