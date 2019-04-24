# date:2019-4-22
# author:Ivo Wang
# describition:第一阶段复习。
# editor for code: vs code

# 单行 多行注释

# 这是一个单行注释。

'''这是
多行注释'''

# 变量
# 定义变量

# [变量名] = [值]
# 第一次是定义变量，次后均为使用变量。
# 变量命名规则：使用驼峰命名法，可使用数字、字母及下划线的组合，不允许以数字和下划线开头。

# print输出

# 格式化输出：
# %s：字符串；%d：数字

a = 18
print('he is %s years old'%a)

# 两个及以上占位符

a = 18
b = 'Ivo Wang'
print('%s is %d years old'%(b,a))

# 打印完毕不换行的方法。
a = 'aaaa'
b = 'bbbb'
print(a,end= '')
print(b)

# 查看帮助文档
# helo([方法名])
help(print)

# input 输入

userName = input('请输入用户名：')
print('您刚输入的用户名为：%s'%userName)

# 运算符
# 取余 %
print(10 % 3)
# 幂 **
print(2 ** 3)
# 赋值运算符 =
a = 18
b = 20 
a,b = b,a
print(a,b)
# 复合运算符
a = 0
a += 1
print(a)

# if 判断语句及嵌套
userAge = int(input('请输入您的年龄：'))
if userAge < 16:
    print('正直青春年少')
else:
    if userAge <25:
        print('年轻')
    else:
        print('油腻大叔')

# while 循环

i = 0
while i < 3:
    print(i)
    i+=1
print('action')

# break 语句
while True:
    if input('输入一个数字或者q退出') != 'q':
        print('helloworld')
    else:
        break

# for 循环及continue语句
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# 字符串常见操作
# 1、查找 find index rfind rindex
myStr = 'hello python'
print(myStr.find('l'))
print(myStr.index('o'))
print(myStr.rfind('p'))
print(myStr.rindex('y'))

# count 统计
myStr = 'hello python'
print(myStr.count('l'))

# replace 替换

myStr = 'hello python'
print(myStr.replace('h','H'))
print(myStr.replace('h','H',1))

# split 分割
myStr = 'hello python'
print(myStr.split(' '))

# captialize 首字母大写
myStr = 'hello python'
print(myStr.capitalize())

# title 将所有首字母大写
myStr = 'hello python'
print(myStr.title())

# starwith endwith 以xx开头 以xx结尾，返回结果True或False
myStr = 'hello python'
print(myStr.startswith('h'))
print(myStr.endswith('h'))

# lower 将所有字母小写
# 最常见使用：验证码不区分大小写。
myStr = 'HELLO PYTHON'
print(myStr.lower())

#upper大写
myStr = 'hello python'
print(myStr.upper())

# ljust rjust center 左对齐、右对齐、居中对齐并填充长度
myStr = 'hello python'
print(myStr.ljust(100))
print(myStr.rjust(100))
print(myStr.center(100))

# strip 清除字符串前后的空格
myStr = '     hello python     '
print(myStr.strip())

# partition 以xx分割字符串.
myStr = 'hello python'
print(myStr.partition('l'))

# 列表
# append 增加
myList = [1,2,3,'hello',1.1]
myList.append('world')
print(myList)
# extend 表末尾一次性追加另一个序列中的多个值
myList.extend('haha')
print(myList)
# insert 指定位置插入
myList = [1,2,3,'hello',1.1]
myList.insert(0,'he')
print(myList)
# 改 通过索引修改
myList = [1,2,3,'hello',1.1]
myList[0] = 2
print(myList)

# 查 in not in index  count
# 无find 方法
myList = [1,2,3,'hello',1.1]
print(1 in myList)
print(1.1 not in myList)
print(myList.index(2))
print(myList.count(2))

# 删 del remove pop
myList = [1,2,3,'hello',1.1]
del myList[0]
print(myList)
myList = [1,2,3,'hello',1.1]
print(myList.remove(2))
myList = [1,2,3,'hello',1.1]
myList.pop()
print(myList)
# 列表遍历
myList = [1,2,3,'hello',1.1]
for temp in myList:
    print(temp)

# 列表排序
# 从小到大排序
newList = [1,31,9,4,7,15]
newList.sort()
print(newList)
# 从大到小排序
newList = [1,31,9,4,7,15]
newList.sort(reverse = True)
print(newList)
# 列表扭转
newList = [1,31,9,4,7,15]
newList.reverse()
print(newList)

# 元组
# 元组与列表类似，不同在于元组元素不能修改
# 元组如果只有一个值时，需要加,

myTuple = ('heihei',)
print(myTuple)

# 字典
# 键值对，key不允许重复

# 查
myInfo = {'name':'wang','sex':'f','wife':'none'}
print(myInfo['name'])
print(myInfo.get('name'))

# 改
myInfo = {'name':'wang','sex':'f','wife':'none'}
myInfo['wife'] = 'li'
print(myInfo)

# 增
# [变量名][[key值]] = [value]
myInfo = {'name':'wang','sex':'f','wife':'none'}
myInfo['age'] = '18'
print(myInfo)

# 删
# del 
myInfo = {'name':'wang','sex':'f','wife':'none'}
del myInfo['wife']
print(myInfo)
# clear
myInfo = {'name':'wang','sex':'f','wife':'none'}
myInfo.clear()
print(myInfo)

# 复制
myInfo = {'name':'wang','sex':'f','wife':'none'}
myNewInfo = myInfo.copy()
print(myNewInfo)

# 字典长度
myInfo = {'name':'wang','sex':'f','wife':'none'}
print(len(myInfo))

# 输出字典所有key
myInfo = {'name':'wang','sex':'f','wife':'none'}
print(myInfo.keys())

# 输出字典所有value
myInfo = {'name':'wang','sex':'f','wife':'none'}
print(myInfo.values())

# 输出字典所有键值对
myInfo = {'name':'wang','sex':'f','wife':'none'}
print(myInfo.items())