# 编写一个函数用于计算从start开始到end结束之间所有的数字的累加和
# 1.当函数执行到return的时候就会马上终止函数执行
# 2.函数中可以出现多个return，但是有且只有一个return会被执行
# return后面可以不跟值，return单独使用等价于return None


def lei_jia(start, end):
    # 判断start end是否都是数字
    my_type = isinstance(start, int)
    # 假
    if not my_type:
        print('start 应该是一个数字！')
        return

    is_int = isinstance(end, int)
    if not is_int:
        print('end 应该是一个数字！')
        return None

    if start > end:
        print('start 应该小于 end！')
        return None

    i = start
    my_sum = 0
    while i <= end:
        my_sum += i
        i += 1

    print(my_sum)


lei_jia(2, 30)

