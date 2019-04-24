# date:2019-4-13
# author：Ivo wang
# describtion ： 条件语句、语句、术语表及练习

# 条件语句
# 关键字if、elif和else用于条件语句
# 是一种控制结构：通过分析变量值从而做出对应决定的代码块。
# 语法：
'''if xxx:
    (code_area1)
else:
    (code_area1)'''
# 例：
country = 'US' 
if country == 'US':
    print('hello,US')
else:
    print('hello,world')

# 可单独使用一个if语句
# 但else无法单独使用：
if country == 'US':
    print('わだしわ')

# 也可以连续使用if语句：
x = 2
if x == 2:
    print('the number is 2.')
if x % 2 == 0:
    print('the number is even.')
if x % 2 != 0:
    print('the number is odd.')

# 也可以使用if语句中再加入一个if语句（嵌套）
# 当两个if判断均为True时，执行print语句
y = 3
if True:
    if y >= 3:
        print('y大于等于3')

# elif：如果if-else语句中包含elif语句，首先执行if语句
hometown = 'shandong'
if hometown == 'shandong':
    print('it is shandong')
elif hometown == 'shanxi':
    print('it is shanxi')
else:
    print('no idea')
# 如果if 和elif语句求值结果均不为True，则执行else
hometown = 'shandong'
if hometown == 'pek':
    print('it is pek')
elif hometown == 'shanxi':
    print('it is shanxi')
else:
    print('no idea')

# 语句
# 定义：描述语言的多种结构部分，分为简单语句和复合语句。

# 简单语句：一般就是一行代码。如：
print('hello world')

# 复合语句：由一个或者多个从句组成
# 从句包含代码头及紧随其后的配套代码
# 代码头：从句中包含关键字的哪行代码
# 配套代码：所今后的代码
# 复合语句如：
for i in range(100):
    print('hello world')

# 相关术语整理：
# 条件语句：根据条件执行不同代码的代码。
# 控制结构: 通过分析变量的值，来决定代码如何执行的代码块。
# 伪代码： 用来掩饰逻辑的标记方法，与代码类似。
# if-else语句：用来表达'如果出现这种情况，则这样做，否则那样做'的方法。
# if语句：if-else语句的第一部分。
# else语句：if-else语句的第二部分。
# 语句：一个命令或者计算。
# 简单语句：可用一行代码表示的语句。
# 复合语句：通常包含多行代码的语句。
# 从句：复合语句的组成部分；一个从句由两行或者多行代码构成，包含代码头及配套语句。
# 代码头：从句中包含关键字的哪行代码，之后是一个冒号和一行或多行带缩进的代码。
# 配套代码：从句中由代码头控制的代码。

# 练习
# 1、打印3个不同的字符串。
print('hello world')
print('わだしわ')
print('11111')
# 2、编写程序：如果变量值小于10，打印一条消息；如果大于或等于10，则打印不同的消息
a = 10
if a < 10:
    print('a的值小于10')
else:
    print('a的值大于等于10')

# 3、编写程序：如果变量的值小于或等于10，打印一条消息；如果大于10且小于或者等于25，
# 则打印一条不同的消息；如果大于25，则打印另一条不同的消息；
b = 15
if b <= 10:
    print('小于等于10')
elif b > 10 and b <= 25:
    print('大于10且小于等于25')
elif b > 25:
    print('大于25')
# 4、将两个变量相除，打印余数。
c = 10
d = 3
print(c % d)
# 5、编写一个将两个变量相除，打印商
e = 20
f = 2 
print(e / f)

# 6、编写一个程序，为变量age赋予一个整数值，根据不同的数字打印不同的字符串说明。

age = int(input('请输入年龄：'))
if age == 10:
    print('外傅之年')
elif age == 20:
    print('弱冠之年')
elif age == 30:
    print('而立之年')
elif age == 40:
    print('不惑之年')
elif age == 50:
    print('知天命之年')
elif age == 60:
    print('花甲之年')
elif age == 70:
    print('古稀之年')
elif age == 80 or age == 90:
    print('耄mao耋die之年')
elif age == 100:
    print('期颐')
else:
    pass
# 需要补充6题的第一行代码，input获取键盘输入的内容类型为str
# 所以要将内容通过str关键字进行转换，否则无法执行下面的条件语句。
a = 10.1
print(type(a))