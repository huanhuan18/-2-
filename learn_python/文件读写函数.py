# 写文件  write  writelines

def test01():
    """writelines 函数用法"""
    f = open('test1', 'w')
    # writelines 一次可以写多行，参数是一个列表，列表每一个元素都是一行数据
    lines = ['aaa\n', 'bbb\n', 'ccc\n']
    f.writelines(lines)
    f.close()


def test02():
    """读操作"""
    f = open('test2.txt', 'r')
    # read 指定参数，则读取指定个数的数据
    content = f.read(5)
    print(content)
    f.close()


def test03():
    """一次读取一行"""
    f = open('test2.txt', 'r')
    content1 = f.readline()
    content2 = f.readline()
    print(content2)
    f.close()


def test04():
    """一次读取所有行"""
    f = open('test2.txt', 'r')
    # content = f.readlines()
    # print(content)
    for line in f.readlines():

        if line[-1] == '\n':
            print(line[:-1])
        else:
            print(line)

    f.close()

# test01()
# test02()
# test03()
test04()