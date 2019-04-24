# date:2019-4-14
# author：Ivo wang
# describtion ： 函数、定义函数、内置函数、复用函数、
#                必选及可选参数、作用域、异常处理、文档字符串
#                有需要才使用变量、术语表、挑战练习
# editor: vs code

# 函数
# 定义：可接受输入，执行指令并返回输出的符合语句。

# 定义函数：
#def [函数名]([参数])：
#    [函数定义]
# def 关键字后，指定函数名称，名称定义遵循变量的定义规则。
# 函数名称后添加括号，括号中为希望函数接收的参数。
# 如：f(x) = x * 2函数的定义方式

'''def f(x):
    return x * 2

# 调用函数的方法[函数名]([逗号分隔的参数])，如调用上面的函数：

f(3)

# 如果函数有返回值，可将函数的返回值存入一个变量并打印。

result = f(3)
print(result)

# 函数可以有多个参数，也可以不接收参数。如

def f1():
    return 1 + 1
result = f1()
print(result)

# 如果函数要接收多个参数，则必须将圆括号内的参数以逗号相隔，如：

def f2(x,y,z):
    return x + y + z
result = f2(1,2,3)
print(result)

# 函数必须包含return语句，否则输出结果为none，如;

def f3():
    z = 1 + 1
result = f3()
print(result)

# 内置函数
# 内置函数指编程语言中自带的函数，执行各式各样的计算和任务
# 如print函数、len函数等

a = 'hello world'
print(len(a))

# 内置函数str接受一个对象作为参数并返回一个数据类型为str的新对象。

b = 100
print(type(b))
str(b)
print(type(b))

# int函数可接受一个对象作为参数，并返回一个整型对象。
# float函数可接受一个对象作为参数，并返回一个浮点数对象。
# 传给str、int、float的参数，必须能转换成字符串、整数、浮点数。
# str可接受大部分对象作为参数；int只能接受内容为数字的字符串或浮点数；
# float只能接受内容为数字的字符串和整型对象
# 如：
print(int('100'))
print(int(20.1))

print(float('100.01'))
print(float(66))

# 如果传递的参数无法转换，如：

# print(int('hello world'))

# 报错：ValueError: invalid literal for int() with base 10: 'hello world'

# 转换类型可使用在用户需要获取键盘输入并与某个对象做比较时统一类型
# 如获取用户年龄并判断年龄所处范围：

age = input('请输入您的年龄：')
int_age = int(age)
if int_age >= 21:
    print('老家伙')
else:
    print('小青年')


# 复用函数
# 函数不仅可以计算并返回值，还可以封装复用的功能。
# 如判断一个数是奇数还是偶数：

def even_odd(x):
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
even_odd(2)
even_odd(3)


# 必选及可选参数
# 函数可接受两种参数：必选参数和可选参数
# 可选参数：只在函数输入时才会传入，并不是函数执行所必须的。
# 定义可选参数的语法：[函数名](p[参数名]=[参数值])
# 与必选参数一样，两个及以上可选参数也需要用逗号隔开
# 单个可选参数如：

def f4(x = 2):
    return x ** x
print(f4())
print(f4(4))

# 多个可选参数如：
def f5(x = 3,y = 5):
    return x + y
print(f5())
print(f5(4,6))


# 作用域
# 定义：定义变量时，其作用域指定的是哪部分程序可对其进行读写。
# 如果在函数外定义的变量，则变量拥有全局作用域(global scope)：
# 即在程序的任意一个地方都可对其进行读写。
# 全局变量(global variable)：拥有全局作用域的变量
# 如果在函数或者类内部定义一个变量拥有局部作用域：
# 即：程序只有在定义该变量的函数内部才能对其进行读写。
# 全局变量如：

a = 1
b = 2
c = 3
def f6():
    print(a)
    print(b)
    print(c)
f6()

# 在函数内定义的局部变量，如果尝试在函数外访问，python会报异常错误。如：
def f7():
    x = 1
    y = 2
    z = 3
f()
print(x)
print(y)
print(z)

# 局部作用域中对全局变量进行写操作，需要使用使用global关键字，并声明希望修改的变量名，如：

x = 100
def f8():
    global x
    x += 1
    print(x)
f8()


# 异常处理
# 假设一个通过键盘获取除数和被除数，如果除数获取为0，则会报异常
# 解决方法就叫异常处理
# 处理异常使用try和except关键字，如果用户除数输入0，会打印不要输入0的提示。
# 如：

a = int(input('请输入被除数：'))
b = int(input('请输入除数：'))
try:
    print( a / b)
except ZeroDivisionError:
    print('除数不能为0')

# 如果用户输入是无法转换成无法转换成整型的字符串，程序也会报异常： 
# 解决方法将收集用户输入的代码放入try语句内，并让except捕获ZeroDivisionError和ValueError异常：
# 例：

try:
    a = int(input('请输入被除数：'))
    b = int(input('请输入除数：'))
    print(a / b)
except (ZeroDivisionError,ValueError):
    print('非法输入')

# 注意:不要再except中使用try中定义的变量。
# 如：

try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print(c)

# 异常提示：NameError: name 'c' is not defined

# 文档字符串
# 定义：在编写函数时，在函数顶部留下解释每个参数的参数类型的注释
# 如：
def add(x,y):
    
    返回x + y的值
    :param x: int
    :param y: int
    :return: int,x与y之和
    
    return x + y

# 有需要时才使用变量
# 不要仅仅为了打印某个值就将数值保存至变量。

# 术语表整理

# 函数:可接受输入和执行的指令，并返回输出的复合语句。
# 惯例：普遍认可的行为方式。
# 调用：向函数提供执行指令、返回输出所需要的输入。
# 参数：传递给函数的数据。
# 必选参数：非可选参数。
# 可选参数：非必选参数。
# 内置函数：python自带的函数。
# 作用域：变量可读写的范围。
# 全局作用域：可在程序中任意位置读写的作用域。
# 全局变量：拥有全局作用域的变量。
# 局部作用域：只能在其定义的函数（类）中读写变量的作用域。
# 异常处理：检测错误条件，如果符合则捕获异常，并决定如何处理。
# 文档字符串：解释函数功能，记录参数类型的字符串。

# 练习
# 1、编写一个函数，接受数字作为输入，并返回该数字的平方。

def square(x):
    result = x ** 2
    return result
x = input('请输入一个数字：')
int_x = int(x)
square(int_x)

# 2、编写一个以字符串为参数并将其打印的参数。

def str_prt(y):
    print(y)
y = input('请输入一个字符串:')
str_prt(y) 

# 3、编写一个接受3个必选参数、2个可选参数的函数.

def mand_opti(a,b,c,d=1,e=2):
    return a + b + c + d + e
mand_opti(3,4,5)

# 4、编写一个带俩函数的程序。第一个函数接受一个整数为参数，并返回该整数除以2的值。
# 第二个函数接受一个整数为参数，并返回该整数乘以4的值。调用第一个函数，将结果保存至变量
# 并将变量作为参数传递给第二个函数。
def f9(x):
    result = x / 2
    return result

def f10(y):
    result = y * 4
    return result

x = input('请输入一个整数：')
int_x = int(x)
y = f9(int_x)
print(f10(y))'''

# 5、编写将一个字符串转换为float对象并返回结果的函数，使用异常处理来捕获可能发生的异常。
def f11(x):
    result = float(x)
    return result  
try:
    my_str = input('请输入一个字符串')
    f11(my_str)
except ValueError:
    print('请不要输入字母及符号')
b = 100
b = str(b)
print(type(b))