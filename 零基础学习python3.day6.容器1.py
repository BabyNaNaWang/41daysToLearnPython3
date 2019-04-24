# date:2019-4-16
# author:Ivo Wang
# describition:字典、容器嵌套、容器术语表、挑战练习
# editor for code: vs code

# 1、字典
# 概念：字典是另一个用于存储对象的容器，他们链接键(key)和值(value)这两个对象。
# 映射：将一个对象链接至另外一个对象，称为映射(mapping)。
# 键值对：映射结果产生键值队(key-value pair)
# 字典是可变的，即可向字典中新增键值对。

# 创建字典的方法有两种，第一种：通过dict函数

my_dict = dict()
print(my_dict)

# 第二种：通过大括号赋值给变量

my_dict = {}
print(my_dict)

# 在创建字典时直接添加键值对的方法：[字典名] = {[key]:[value],[key1]:[value]}
# 如创建一个个人信息的的字典：

person_info = {'name':'王二小','age':'18'}
print(person_info)

# 创建字典后添加键值对的方法：[字典名][[key] = [value]

person_info = {'name':'王二小','age':'18'}
person_info['sex'] = 'male'
print(person_info)

# 查找键对应值的方法：[字典名][[键值]]

person_info = {'name':'王二小','age':'18'}
print(person_info['name'])

# 需要注意的点：
# 1、字典的值可以是任意对象
# 2、字典的键(key)必须是唯一且不可变的
# 3、字符串可以作为字典的键，但列表或字典不可以。

# 可通过in 和not in 检查某个键值是否在字典中：

person_info = {'name':'王二小','age':'18'}
print('sex' in person_info)
print('sex' not in person_info)

# 访问一个不在字典中的键值，python会报错。

#person_info = {'name':'王二小','age':'18'}
#print(person_info['sex'])

# 删除键值对的方法：del [字典名][[键值]]

person_info = {'name':'王二小','age':'18'}
del person_info['age']
print(person_info)

# 应用实例：班级信息表中查询某学生是否存在，如果存在则打印其姓名，如果不在则提示不在。

'''student_info = {'王二小':'18','小红':'19','小明':'17'} 
name = input('请输入学生名称:')
if name in student_info:
    print(student_info[name])
else:
    print('未找到该学生')'''

# 容器嵌套
# 容器嵌套指在容器中存储容器

# 列表嵌套：

'''my_list = []
list1 = [1,2,3]
list2 = [4,5,6]
my_list.append(list1)
my_list.append(list2)
print(my_list)'''

# 可通过索引访问列表中的列表

#print(my_list[0])

# 嵌套列表中增加元素，则该修改也会在最外层列表中。

my_list = []
list1 = [1,2,3]
list2 = [4,5,6]
my_list.append(list1)
my_list.append(list2)
list1.append(8)

print(list1)
print(my_list)

# 也可以在列表中存储元素，在元祖中存储列表，还可以在列表或元组中存储字典
# 字典或元组可称为字典的值。[字典名]={[key]:[list],[key]:[tuple]}

# 术语表
# 方法：与指定数据类型紧密相关的函数。
# 列表：存储有序对象的容器。
# 可迭代的：如果使用循环访问对象中的每一个元素，则该对象是可迭代的。
# 可迭代对象：可迭代的对象，如字符串、列表和元素。
# 索引：代表元素在可迭代对象中位置的数字。
# 可变的：容器中的内容可以发生变化。
# 不可变的：容器中的内容不能改变。
# 字典:存储兑现的一种内置容器，将一个称为键的对象，映射至一个称为值的对象。
# 键：用来查找字典对应的值。
# 值：字典中映射至键的值。
# 映射：将一个对象连接至另一个对象。
# 键值对：字典中键映射值。

# 练习
# 1、创建一个你喜欢歌手的列表。

singer = ['崔健','许巍','朴树','郑钧','李志']

# 2、创建一个由元组构成的列表，每个月组包含居住过或旅游过的城市的经纬度。

cities = [(104.10194,30.65984),(120.39629,36.30744)]

# 3、创建一个你的不同属性的字典:姓名、喜欢的颜色和喜欢的作者。

my_info = {'姓名':'王二小','最喜欢的颜色':'蓝色','最喜欢的作者':'还没有'}

# 4、编写一个程序，让用户询问你的姓名、最喜欢的颜色或最喜欢的作者，并返回上一个
# 挑战中创建的字典中对应的值.

question = int(input('请输入你希望了解的我的信息：1、姓名；2、喜欢的颜色；3、喜欢的作者：'))
if question == 1:
    print(my_info['姓名'])
elif question == 2:
    print(my_info['最喜欢的颜色'])
elif question == 3:
    print(my_info['最喜欢的作者'])
else:
    print('查无此项')

# 5、创建一个字典，将一个歌手映射至你最喜欢的歌曲。

singer_song = {'崔健':['假行僧','花房姑娘','对面的妞','新长征路上的摇滚'],
'许巍':['故乡','蓝莲花'],'李志':['梵高先生','关于郑州的回忆']}
print(singer_song)
