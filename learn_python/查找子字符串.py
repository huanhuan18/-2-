# user_email = 'nakelulu@itcast.cn'
# 1.找到字符串中@的位置
# 2.获得字符串中的子串

user_email = 'nakelulu@itcast.cn'
# 如果查找到，返回子串第一次出现的位置
# 如果查找不到@， 返回 -1
position = user_email.find('@')
if position == -1:
    print('@不存在，邮箱不合法！')
else:
    username = user_email[:position]
    houzhui = user_email[position+1:]
    print('用户名是：', username)
    print('邮箱后缀：', houzhui)