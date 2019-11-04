user_name = input('请输入你要注册的用户名：')
# strip函数默认去除字符串两侧的空格
new_username = user_name.strip()

print(new_username)
# isalpha 判断字符串所有元素是否都是字母
if new_username.isalpha():
    print('注册成功！')
else:
    print('注册失败！')

# isdigit 判断是否是数字