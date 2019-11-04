import os

def file_rename():
    """文件重命名"""
# os模块中的rename()可以完成对文件的重命名操作

    os.rename('test2.txt.bk', 'hello.txt')


def file_remove():
    """文件删除"""
    os.remove('/users/edw/desktop/a.txt')

# 路径问题  如果只写文件名，默认只在当前目录下找文件，如果找不到就报错

def test03():
    """创建和删除目录"""
    os.mkdir('user/edw/desktop/aaa')
    os.rmdir('user/edw/desktop/aaa')

def test04():
    """获得指定目录下的文件列表"""
    content = os.listdir()
    print(content)

def test05():
    """获得和设置工作目录"""
    cwd = os.getcwd()   #current working directory
    print(cwd)
    # 将默认的工作目录设置到我的桌面
    os.chdir('/user/edw/desktop')

# file_rename()
# file_remove()
# test03()
# test04()
# test05()