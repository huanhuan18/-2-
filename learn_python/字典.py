# 1.字典定义
# 字典注意点：
# 1.1字典的键不能重复，值是可以重复
# 1.2字典是非序列式容器，不支持索引，也不支持切片


def test01():
    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    print(my_dict['name'])
    print(my_dict[101])   # key 关键字    value 值
    my_dict['gender'] = '女'
    print(my_dict)


def test02():
    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    # 使用中括号这种访问字典中元素的方式，如果键不存在则会报错，程序终止。
    # print(my_dict['age1'])
    #   使用 get 方法, 如果key 不存在默认返回None，也可以指定默认返回值

    print(my_dict.get('age1', '我是默认值'))

def test03():
    """添加和修改元素"""
    my_dict = {'name': 'Obama', 'age': 18, 'gender': '男', 101: 100}
    my_dict['score' = 99]  #添加新元素
    print(my_dict)
    # 如果key 不存在则是新增元素，存在的话就是修改元素

test01()
test02()
test03()