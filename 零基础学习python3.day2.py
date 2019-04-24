# date:2019-4-11
# author：Ivo wang
# describtion ： 语法、错误与异常、算数操作符、逻辑操作符、比较操作符

# 语法
# 定义：指规范一门语言中句子结构，尤其是字词顺序的一整套规则及流程
# 例：字符串永远被包含在引号内
'''print('hello world')

# 错误与异常

# 错误
# 代码不遵循语法，运行时将出现错误，代码无法执行，并给出错误信息
# 例：只使用一个引号定义字符串
myStr = 'hello world.
# 语法错误会提示：EOL while scanning string literal

# 缩进错误
a = 100
    b = 100
#缩进错误提示：unexpected indent

# 异常
# 定义：不属于语法错误的错误，称为异常。
# 例：以0作为除数，则会出现异常
a = 10 / 0
print(a)
# 提示异常：ZeroDivisionError: division by zero
# 常见异常如：https://www.cnblogs.com/fclbky/articles/4098151.html

# 算数操作符
# 定义：支持数学运算的操作符

# 指数运算：**
print(2.1 ** 2)

#取模运算(取余运算): %
print(10 % 3)

# 整除运算: //
print(13 // 8)

# 除法运算: /
print(13 / 8.0 )

# 乘法运算: *
print(2.0 * 3)

# 减法运算：-
print(6 - 4)

# 加法运算：+
print(6.0 + 4) 

# 操作数
# 定义：操作符两侧的值称为操作数

# 表达式
# 定义：两个操作数和一个操作符共同构成一个表达式

# 运算顺序
# 遵循与数学表达式求值相同的运算顺序'''

'''# 比较操作符
# 比较操作符的求值结果只有True和False

# 大于：>
print(100 > 10)

# 小于: <
print(100 < 10)

# 大于等于:>=
print(100 >= 10)

# 小于等于
print(100 <= 10)

# 等于: ==
print(100 == 10)

# 不等于：!=
print(100 != 10)'''

#逻辑操作符

# 逻辑操作符的求值结果也是True和False

# 与：and 
# 可以连接两个以上表达式，如果两者求值均为False，则返回False;
# 如果两者求值有一个或者均为False 则返回False

print(1 == 1 and 2 == 2)

print(1 == 2 and 2 == 2)

print(1 == 2 and 2 == 1)

# 或：or 
# 可以连接两个以上表达式，如果两者求值均为True，则返回True;
# 如果两者求值有一个或者均为False 则返回False

print(1 == 1 or 2 == 2)

print(1 == 2 or 2 == 2)

print(1 == 2 or 2 == 1)

# 非：not 
# 将关键字not放在表达式前面，取表达式求值结果的对立值
# 如果表达式求值结果为True，则加上not后结果变为false

print(not 1 == 1 )

print(not 1 == 2 )
