my_list = [10, 20, 30, 40]

old_value = 30
new_value = 200

# index 用于根据值查询
# index 如果查找不到值，程序就会终止，直接报错，所以用if语句来写
if old_value in my_list:
    # 查找到值为 old_value 的位置
    pos = my_list.index(old_value)
    # 根据位置修改值
    my_list[pos] = new_value

print(my_list)

my_list2 = ['aaa', 'bbb', 'ccc']

# 将一个列表中的所有元素追加到当前列表的尾部
my_list.extend(my_list2)
print(my_list)