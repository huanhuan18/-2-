my_dict = {'aaa': 10, 'bbb': 20, 'ccc': 30}

# 默认只能遍历出来键
# for val in my_dict:
#     print(val)

# keys 方法可以获得所有的键值对列表，每一个键值对都是一个元组
key_list = my_dict.keys()
print(list(key_list))  #转换成列表形式

value_list = my_dict.values()
print(list(value_list))

key_value_list = my_dict.items()
print(list(key_value_list))

for key_value in key_value_list:
    print('key:', key_value[0], 'value:', key_value[1])