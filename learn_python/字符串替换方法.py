poetry = '床前明月光，疑是地上霜。举头望明月，低头思故乡。举'

# replace并不会替换原来的字符串， 替换完毕之后返回一个新的字符串
new_poetry = poetry.replace('举', '歌')
print(poetry)
print(new_poetry)

new_poetry = poetry.replace('举', '歌', 1)
print(new_poetry)

# 容器专属方法（函数）
# 字符串通过点的方式调用专属的函数

# 字符串的特点：
# 1.字符串一旦定义不允许修改
# 2.字符串容器中的元素都是字符类型的