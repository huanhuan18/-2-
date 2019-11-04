# 1.获得要拷贝的文件名
old_file_name = input('请输入您要拷贝的文件名:')   #test2.txt  ->  test2.txt.bk
# 2.读取要拷贝的文件内容
new_file_name = old_file_name + '.bk'
# 3.打开新的文件
f_old = open(old_file_name, 'rb')
f_new = open(new_file_name, 'wb')
# 4.将老文件内容写到新文件里面
old_file_content = f_old.read()
f_new.write(old_file_content)
# 5.关闭新老文件
f_old.close()
f_new.close()