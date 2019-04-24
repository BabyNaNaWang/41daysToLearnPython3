# date:2019-4-17
# author:Ivo Wang
# describition:容器集合、三引号字符串、索引、字符串是不可变的、字符串拼接
# editor for code: vs code

# 容器集合
# 定义：集合（set）是一个无序的不重复元素序列。
# 集合中的元素必须是不可变类型的
# 创建集合的方法有两种：

# 第一种：通过set(value)创建空集合

my_set = set('hello')
print(my_set)

# 第二种：通过{value,value1}方式创建

my_set = {1,2,3,3}
print(my_set)

# 定义不可变集合: [变量名] = frozenset([已创建集合变量])

n_my_set = frozenset(my_set)
print(n_my_set)

# 集合间运算

# 子集判断：< 或 issubset()

my_set1 = {1,2,3,4,5}
my_set2 = {7,8,9,10}
my_set3 = {2,3}
print(my_set3 < my_set1)
print(my_set3 < my_set2)
print(my_set3.issubset(my_set1))
print(my_set3.issubset(my_set2))

# 并集运算:丨 或 union()

my_set1 = {1,2,3,4}
my_set2 = {5,6,7}
print(my_set1 | my_set2)
print(my_set1.union(my_set2))

# 交集：& 或 intersection()

my_set1 = {1,2,3,4}
my_set2 = {3,5,6,7}
print(my_set1 & my_set2)
print(my_set1.intersection(my_set2))

# 差集(所有属于一个集合且不属于另一个集合元素构成的集合)：- 或 difference()

my_set1 = {1,2,3,4}
my_set2 = {3,5,6,7}
print(my_set1 - my_set2)
print(my_set1.difference(my_set2))

# 对称差(只属于其中一个集合，而不属于另一个集合的元素组成的集合): ^ 或者 symmetric_difference()

my_set1 = {1,2,3,4}
my_set2 = {3,5,6,7}
print(my_set1 ^ my_set2)
print(my_set1.symmetric_difference(my_set2))

# 集合中添加元素：add

my_set = {1,2,3}
my_set.add(4)
print(my_set)

# 清空集合中的元素：clear

my_set = {1,2,3}
my_set.clear()
print(my_set)

# 复制：copy

my_set = {1,2,3}
n_my_set = my_set.copy()
print(n_my_set)

# 随机删除:pop

my_set = {'h','l','w'}
my_set.pop()
print(my_set)

# 移除：remove,如果删除元素不存在则报KeyError

my_set = {'h','l','w'}
my_set.remove('l')
print(my_set)

# 添加其他集合/列表:update

my_set = {1,2,3}
my_set.update({4,5,6})
print(my_set)

# 还有其他方法，详情参考
# https://www.cnblogs.com/suendanny/p/8597596.html

# 三引号字符串
# 如果字符串需要跨一行以上，可以使用三引号

my_str = '''第一行
第二行
第三行'''
print(my_str)