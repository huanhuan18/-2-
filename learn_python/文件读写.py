# 打开文件
fa = open('test1.txt', 'w')
# fb = open('test2.txt', 'w')

my_content = 'hello world! 第一次写入文件!\n'
fa.write(my_content)

# 关闭文件
fa.close()

# 读取文件数据
fb = open('test2.txt', 'r')
# read 函数默认读取文件中所有数据
my_content1 = fb.read()

fb.close()

print(my_content1)