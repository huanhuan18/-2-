#计算1-100之间所有数的累加和

i = 1
total = 0
#
# total = total + i
# start += 1

while i <= 100:
    total = total + i
    i += 1

print('总和：',total)

#计算1-100之间所有奇数和
i = 1
my_sum = 0
while i <= 100:
    if i % 2 == 1:
        my_sum = my_sum + i
    i += 1

#打印星星
"""
*
**
***
****
*****
"""
i = 1
while i <= 5:
    print('*' * i)
    i += 1