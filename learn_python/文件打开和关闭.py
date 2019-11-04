"""1.文件打开分为两种： 文本模式   二进制模式
 r w a   rb  wb  ab
 Linux操作系统：akdakfjdflaf\n
 mac操作系统：fsdjssljfskdjjljsd\r
 windows:akjdlafdlsadflsad\r\n
 程序： hello world\n  程序里面换行符就是\n
         -> windows  hello world\r\n
         -> mac      hello world\r
         -> linux    hello world\n
 打开文件用的是文本模式，会进行换行符的转换
 打开文件用的是二进制模式的话，不会进行换行符转换
文件不管是文本还是二进制，在磁盘中的存储都是01011011001010101
"""
"""在python中，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，使用close来关闭一个文件"""

# 打开文件
fa = open('test.txt', 'w')
# 关闭文件
fa.close()