# date:2019-4-19
# author:Ivo Wang
# describition:字符串连接、去空格、替换、查找索引、术语表、练习
# editor for code: vs code

# 字符串连接 join
# join方法可以在字符串的每个字符间添加新的字符。
# 如：

a = 'hello'
print('+'.join(a))

# 也可以在空字符串上调用方法，传入一个字符串列表作为参数
# 将列表中的字符串连接成一个字符串
# 如：

b = ['h','e','l','l','o']
word = ''.join(b)
print(word)

# 还可以在包含空格符的字符穿上，创建一个所有单词均由空格符分割的字符串。
# 如：

my_age = ['I','am','18','years','old']
new_age = ' '.join(my_age)
print(new_age) 

# 去除空格 strip
# 可使用strip去除字符串开头和末尾的空白字符
# 如：

a = '   hello world '
a = a.strip()
print(a)

# 替换 replace
# 在replace方法中，第一个参数为要替换的字符串
# 第二个参数作为用来替换的字符串。
# 如：

a = 'hello world'
a = a.replace('l','L')
print(a)

# 查找索引 index or find
# 可使用index或者find查找某个字符第一次出现索引的值

# index与find在查找结果为正向的时候没有区别，

a = 'hello'
print(a.index('l'))
print(a.find('l'))

# 查询结果是否有匹配时不同：
# index：报错：ValueError substring not found
# find:输出-1

a = 'hello'
# print(a.index('w'))
print(a.find('w'))

# 如果不确定查询结果是否匹配可用异常处理方法

try:
    a = 'hello'
    a.index('w')
except ValueError:
    print('not found')

# 从右侧开始查询 rfind rindex

a = 'hello'
print(a.rfind('o'))
print(a.rindex('o'))
# in 关键字
# 关键字in可检查某个字符串是否在另一个字符串中
# 返回结果为True或False

a = 'h'
b = 'n'
c = 'hello world'
print(a in c)
print(b in c)

# 同样的还有not in
a = 'h'
b = 'n'
c = 'hello world'
print(a not in c)
print(b not in c)

# 字符串转义 \
# 字符串放在单引号或者双引号中，如果字符串中使用了同样的引号，则会出现语法错误
# 可在字符串中使用引号前加反斜杠，即可解决问题。
# 转义定义：指在python中有特殊意义的字符前加上符号，告诉python引号为一个字符，没有特殊意义。
# 如：

a = 'she is \'Lily\'' # 双引号同
print(a)

# 使用不同的引号不会出现这个问题

a = 'she is "Lily"'
print(a)

# 换行符 \n
# 在字符串中加入\n来标识换行

print('I\nam\n18\nyears\nold')

# 切片
# 切片可将一个可迭代对象中元素的的子集，创建为一个新的可迭代对象。
# 语法:[可迭代对象][[起始索引]:[结束索引]]
# 起始索引指开始切片的索引，结束索引指结束索引的位置且不包含结束索引
# 如：

# 字符串切片

a = 'hello'
print(a[1:3])

# 列表切片

a = ['1','2','3','4']
print(a[1:3])

# 如果起始索引为0，则可以留空

a = 'hello'
print(a[:3])

# 同样的，如果截取至结尾，则结束索引留空

a = 'hello'
print(a[3:])

# 如果起始索引和结束索引均留空，则返回原可迭代对象。

a = 'hello'
print(a[:])


# 需要间断取数时，需要用到步长，如：

a = 'hello world'
print(a[0:8:2])

# 将字符串扭转

a = 'hello'
print(a[::-1])

# 其他常见的字符串操作
# https://www.cnblogs.com/yujihaia/p/7468253.html

# 术语表
# 负索引：可用来从右向左查找可迭代对象中元素的索引（必须为一个负数）
# 转义：在python中具有特殊意义的字符（如双引号）前加一个符号，告诉python其只是一个字符，没有其他意义
# 切片：将一个可迭代对象中元素的自己，创建一个新的可迭代对象
# 起始索引：开始切片的索引。
# 结束索引：结束切片的索引。

# 挑战练习

# 1、打印字符串'Camus'中所有的字符串。

# 第一种方法
for temp in 'Camus':
    print(temp)

# 第二种方法
i = 0
while i < len('Camus'):
    print('Camus'[i])
    i += 1

# 2、编写程序，从用户处获取两个字符串，将其插入字符串'Yesterday I wrote a [用户输入1].I sent it to [用户输入2]'中并打印新字符串。

a = input('请输入第一个字符串:')
b = input('请输入第二个字符串：')
print('Yesterday I wrote a {a}.I sent it to {b}'.format_map({'a':a,'b':b}))

# 3、将'aldous Huxley was born in 1984'第一个字符大写。

'aldous Huxley was born in 1984'.capitalize()

# 4、对字符串'where now? who now? when now?'调用一个方法，返回如下的列表['where now?','who now?','when now?']

a = 'where now? who now? when now?'
b = []
for temp in a.split('?'):
    temp.strip()
    b.append(temp+'?')
print(b[:3])

# 5、对列表['the','fox','jumped','over','the','fence','.']变成一个正确的句子，但句号之前不能有空格.

a = ['the','fox','jumped','over','the','fence','.']
a = ' '.join(a)
print(a[:len(a)-2]+a[len(a)-1:])

# 6、将字符串'A screaming comes across the sky.'中所有的's'替换为美元符号。

'A screaming comes across the sky.'.replace('s','$')

# 7、找到字符串'Hemingway'中字符'm'所在的索引.

'Hemingway'.index('m')

# 8、先使用字符串拼接和字符串乘法，创建字符串'three three thee'

('three'+ ' ')*3

# 9、对字符串'it was bright cold day in April,and te clocks were striking thirteen.'进行切片，至保留逗号之前的字符。
a = 'it was bright cold day in April,and te clocks were striking thirteen.'
a = a[:a.find(',')]
print(a)