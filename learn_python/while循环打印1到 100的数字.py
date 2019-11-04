# while循环的场景，有些代码需要循环执行
# 打印1到100的数字

# print(1)
# print(2)
# print(3)
# .....
# print(100)

# 循环次数
# i = 1
# while i <= 100:
#         print(i)
#         i += 1    #在while循环体内
# print('end')

# 打印出1-100之间所有的偶数
# i = 2
# while i <= 100:
#     print(i)
#     i += 2

i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1