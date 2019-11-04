# user_email = 'nakelulu@itcast.cn'
# split 拆分 特别多

my_str = 'aa#b123#cc#dd#'
ret = my_str.split('#')
print(ret)
print(ret[0])
print(ret[3])

user_email = 'nakelulu@itcast.cn'
# 获得@字符串在user_email中出现的次数
char_count = user_email.count('@')
if char_count > 1:
    print('你的邮箱不合法')
else:
    result = user_email.split('@')
    print('用户名：', result[0])
    print('邮箱后缀：', result[1])