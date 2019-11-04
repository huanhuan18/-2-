# my_list = [10, 20, 30, 40]
# 列表是序列式容器，支持索引、切片
# print(my_list[0],my_list[2])
# print(my_list[:2])

# 1.列表的遍历（遍历：每个元素不重复的访问一遍）
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# 2.for循环一般都用于容器中元素的遍历
# for val in my_list:
#     print(val)

# break continue 用在循环中，也可以用在for循环中

my_list1 = [[10, 20, 30], [100, 200, 300], [1000, 2000, 3000]]

i = 0
while i < len(my_list1):
    # my_list[i]是什么类型
    # print(my_list[i])
    j = 0
    while j < len(my_list1[i]):
        print(my_list1[i][j])
        j += 1
    i += 1

print('*' * 30)

for o in my_list1:
    for v in o:
        print(v)