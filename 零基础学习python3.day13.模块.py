import math
import random
import statistics
import keyword
import hello
import module1
import cubed
# date:2019-4-23
# author:Ivo Wang
# describition:模块
# editor for code: vs code

# 模块的定义
# 大型程序分割多个包含Python代码的文件，也称为模块
# Python自带、包含许多重要功能的模块称为内置模块。

# 导入内置模块
# 可使用语法import[模块名]导入模块，将[模块名]替换为希望导入模块的名字。
# 导入模块之后可使用模块中的方法和函数。
# 模块函数的调用方法：[模块名].[方法名]
# Python常用模块：
# https://blog.csdn.net/ruanxingzi123/article/details/82787852

# math模块 
# 求x的y次方
# 首先在文件顶部导入math模块，然后调用pow函数

print(math.pow(2,3))

# random模块

# 取整：1到100中使用randomint函数随机生成一个整数

print(random.randint(1,100))

# 取0至1之间的小数

print(random.random())

# 取范围内随机小数

print(random.uniform(1.1,2.2))

# 随机取一个元素

print(random.choice('hello'))

# 随机取2个元素

print(random.choices([1,2,3,4,5,6],k=2))

# 打乱排序

a = [1,2,3,4,5,6]
random.shuffle(a)
print(a)

# 选取特定数量的元素

print(random.sample('helloworld',3))


# statistics 模块
# 使用statistics模块计算数字组成的可迭代对象的均值、中间值和众数（mode）

# 均值 mean

nums = [1,33,56,33,79,100]
nums = statistics.mean(nums)
print(nums)

# 中值 median

nums = [1,33,56,33,79,100]
nums = statistics.median(nums)
print(nums)

# 众数(出现最多的数) mode

nums = [1,33,56,33,79,100]
nums = statistics.mode(nums)
print(nums)

# keywords 模块
# 检查字符串是否为Python关键字。

print(keyword.iskeyword('for'))
print(keyword.iskeyword('hello'))


# 导入其他模块
# 导入非Python内置模块
# 在本地创建一个Python文件，文件里定义方法
# 导入模块后可调用里面定义的方法。

# 在本地创建一个hello.py的文件
# 创建一个打印hello的方法
'''def print_hello():
    print('hello')'''

# import hello 导入
# 调用print_hello方法

hello.print_hello()

# 文件中的代码，在被别人调用时候不想被执行，可将代码放置在
# if __name__ =='__main__'中
# 如:

# 创建打印hello的module1.py文件
# 如果不把print('hello')放入if __name__ =='__main__'中
# 则导入module模块时就会打印hello
# 放入其中则不打印hello
# 此时需要将module中的代码修改为
if __name__ == 'main':
    print('hello')

# 术语表
# 1、模块：含有代码的Python文件的别称。
# 2、内置模块：Python语言中自带的模块，包含诸多重要的功能。
# 3、导入：编写代码，告诉Python从哪导入计划使用的模块。

# 练习

# 1、调用statistics模块中不同于示例中提到的函数。

num_list = [1,2,45,34,6,7]
print(statistics.pstdev(num_list))

# 2、创建一个cubed模块，在其中写一个函数：接受一个数字作为参数，返回该数字的立方。并在另一个模块中导入并调用该函数。

# 本地创建一个名为cubed.py的文件，输入代码如下
def cubic(x):
    return x**3

x = int(input('请输入一个数字：'))
print(cubed.cubic(x))