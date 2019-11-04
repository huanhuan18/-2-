def my_add(a,b):
    ret = a + b
    return ret

# 保存函数的返回结果
ret = my_add(10,20)
# 使用函数计算的结果，进行下一步的计算
final_result = ret + 100
# 输出最终结果
print('最终结果',final_result)

# print函数和return语句的区别
# 1.print是一个函数，只是一个功能。return是一个语句，和def、if类似
# 2.print会将数据打印到屏幕上，return会将数据返回到程序中，给函数的调用者

# 函数的返回值到底应该有没有？要由你编写的函数功能来决定

#位置参数一定要在关键字参数的前面
#return关键字：
#当函数执行到return的时候就会马上终止函数执行
# 函数中可以出现多个return