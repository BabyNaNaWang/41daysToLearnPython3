# date:2019-4-15
# author:Ivo Wang
# describition:方法、列表、元组
# editor for code: vs code

# 方法：
# 概念：方法是与指定数据类型紧密相关的函数。
# 只有在对象上才能调用函数。
# 也可以传递函数给方法。
# 如：upper(全字符串大写)、replace(替换)方法:

# upper:

print('hello'.upper())

# replace:
print('hello'.replace('h','H'))

# 列表：
# 列表是以固定的顺序保存对象的容器。
# 创建列表的方法有两种：

# 第一种：通过list函数创建列表。

fruit = list()
print(fruit)

# 第二种：直接使用方括号[]

fruit = []
print(fruit)

# 创建有一个有对象的列表，可以使用第二种方法，将对象输入方
# 括号中，以逗号隔开，如：
# 其中'apple'是第一个元素，'banana'是第二个元素，'ananas'是第三个元素

fruit = ['apple','banana','ananas']
print(fruit)

# 可使用append方法将对象加入列表，使用append方法加入的对象永远在列表的末尾。
# 如在fruit列表中添加一个'orange'元素

fruit.append('orange')
print(fruit)

# 可迭代对象定义：如果可以使用循环访问对象中每一个元素，那么对象被称为可迭代对象
# 字符串、列表、元组都是可迭代对象
# 索引：可迭代对象中的每一个元素都有一个索引，即表示元素在可迭代对象中位置的数字。
# 一个可迭代对象的索引值起始值为'0',代表对象的第一个元素
# 获取可迭代对象中元素的方法：[可迭代对象名称][索引]
# 如获取上述fruit列表中第一个元素，即'apple'。

fruit = ['apple','banana','ananas']
print(fruit[0])

# 如果获取的索引值不存在，python会报异常:IndexError
# 如上述fruit列表中有三个元素(可通过len(fruit)查看元素个数)，获取第四个元素

'''fruit = ['apple','banana','ananas']
print(fruit[3])'''

# 可通过索引改变元素中列表的值。
# 如将fruit的第二个元素'banana'变为'watermelon'，如下：

fruit = ['apple','banana','ananas']
fruit[1] = 'watermelon'
print(fruit)

# 可通过pop方法移除列表最后一个元素。

fruit = ['apple','banana','ananas']
target = fruit.pop()
print(target)
print(fruit)

# 不能对空列表使用pop方法，否则会报异常.
'''
new_list = []
new_list.pop()'''

# 可使用加法操作合并两个列表。
list1 = ['he','she']
list2 = ['they','them']
print(list1 + list2)

# 可通过in 和not in 判断某个元素是否在列表中

# in

fruit = ['apple','banana','ananas']
print('watermelon' in fruit)

# not in

fruit = ['apple','banana','ananas']
print('watermelon' not in fruit)

# 使用len获取列表元素个数

print(len(fruit))

# 元组
# 元组是存储有序对象的容器。与列表不同的是，元组是不可变得
# 创建元组后，无法修改其中任何元组的值，也问我无法添加和修改元素
# 元组的创建方法与列表的创建方法相同

#通过tuple函数创建

my_tuple = tuple()

# 通过圆括号创建元组

my_tuple1 = ()

# 注意点：
# 1、即使元组中只含有一个元素，需要在该元素后加逗号
# 2、需要区分数学表达式中的括号与元组括号，数学表达式的括号表明的计算优先级
# 不是元组如：(9)+1

# 创建元组后，不能增加元素或者修改已有元素。
# 如：

'''my_tuple2 = ('what','the')
my_tuple2[0] = 'fxck'
'''

# 与列表相同，可通过索引获取元组内元素

my_tuple = ('you','say','you','love','sunshine')
print(my_tuple[1])

# 与列表相同，也可以通过in 与not in函数查询对象是否在元祖中。

my_tuple = ('you','say','you','love','sunshine')
print('when' in my_tuple)
print('i' not in my_tuple)