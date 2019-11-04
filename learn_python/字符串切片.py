# 字符串提供了一种语法，用来获取字符串中的一个子串

user_email = 'nakelulu@itcast.cn'

print(user_email[0])

# 切片语法 左闭右开
print(user_email[0:4])
print(user_email[0:8])
# 获得容器元素的个数
string_length = len(user_email)
print(user_email[9:string_length])

# 起始值不写表示从0开始
print(user_email[:8])
# 结束值不写表示到最后
print(user_email[9:])
print(user_email[:])

# 步长,第三个数就是隔几个数取一次
print(user_email[0: 8: 2])

# 字符串逆序
print(user_email[::-1])