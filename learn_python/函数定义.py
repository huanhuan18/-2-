
# 函数的好处
#     减少代码的冗余，减少维护量，功能的封装，降低学习成本，提升开发速度

#函数语法

# def 函数名():
#     一行或多行代码

# 如果这个三角星星要打印多次怎么办
# 函数定义
def print_stars():
    i = 1
    while i <= 5:
        print('#' * i)
        i += 1

# 函数定义是不会自动执行的，函数需要调用才能执行
print_stars()


def my_add(a,b):
    ret = a + b
    print('a + b =',ret)

my_add(10,20)