# 创建一个包含10个随机数的列表
import random

my_list = []

i = 0
while i < 10:
    # 产生随机数
    random_number = random.randint(1, 100)
    # 将随机数插入到列表中
    my_list.append(random_number)
    i += 1

print(my_list)
# 对列表中的元素进行排序 sort 排序的意思
# 默认排序是从小到大，升序排序
my_list.sort()
print(my_list)
# 将 sort 函数的 reverse 默认值改成 True 即可实现从大到小排序
my_list.sort(reverse=True)
print(my_list)

# 逆序
my_list.reverse()
print(my_list)

even_numbers = list(range(2, 11, 2))
print(even_numbers)