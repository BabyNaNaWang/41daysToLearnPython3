# date:2019-4-21
# author:Ivo Wang
# describition:continue语句、嵌套循环、术语表、挑战练习。
# editor for code: vs code

# continue语句
# 可使用continue语句来终止循环的当前迭代并进入下一次迭代。
# 如：打印1到5之间除了3之外的数字

for i in range(1,6):
    if i == 3:
        continue
    print(i)

# 也可以通过while循环实现
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# 嵌套循环
# 可通过多种方式将循环组合，当一个循环位于另外一个循环之内时，
# 他就是嵌套在一个循环中。
# 外循环：内部包含循环的循环称为外循环
# 内循环：嵌套的循环称为内循环
# 如：
for i in range(1,3):
    print(i)
    for letter in['a','b','c']:
        print(letter)

# 可用两个for循环将两个列表中的数字相加
# 如

list1 = [1,2,3,4]
list2 = [4,5,6,7]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i + j)
print(list3)

# 可使用while循环和for循环嵌套，实现每次循环征求用户意见是否继续循环那
# 如

while input('是否继续执行？y：继续，n：停止') != 'n':
    for i in range(1,3):
        print(i)

# 术语表

# 循环：在代码中定义的条件未满足之前，将持续执行一段代码。
# 遍历：使用循环访问可迭代对象中的每个元素
# for循环：用来迭代字符串、列表、元组或字典等可迭代对象的一种循环。
# 索引变量：变量的值为代表可迭代对象中索引的一个数字。
# while循环：只要表达式为True则持续执行的一种循环。
# 死循环：永远都不会停止的循环。
# break语句：带关键字break的语句，用来停止循环。
# continue语句：用来终止循环的当前迭代，并进入下一个迭代。
# 外循环：内部包含嵌套循环的循环。
# 内循环：嵌套在另一个循环的循环。

# 练习：

# 1、打印列表['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']中的每个元素

for i in ['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']:
    print(i)

# 2、打印从25到50之间的所有数字。

for i in range(25,51):
    print(i)

# 3、打印['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']中的每个元素及索引

for i,show in enumerate(['The Walking Dead','Entourage','The Sopranos','The Vampire Diaries']):
    print(i,show)

# 4、编写一个死循环和数字列表的程序（可输入Q退出），每次循环时，请用户猜一个数字，然后告知其猜测的是否正确。

num_list = [1,8,20,25,40,90,50]
while True:
    guess_number = input('我这有7个数字，你输一个数，猜猜有没有你这个数或者输入Q退出：')
    if guess_number == 'q':
        break
    elif int(guess_number) not in num_list:
        print('不正确')
    elif int(guess_number)  in num_list:
        print('正确')

# 5、将列表[8,19,148,4]中的所有数字，与列表[9,1,33,83]中的所有数字相乘，并添加至第三个列表。
list_a = [8,19,148,4]
list_b = [9,1,33,83]
list_c = []
for i in list_a:
    for j in list_b:
        list_c.append(i * j)