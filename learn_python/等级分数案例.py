# 根据分数显示档位
"""
1.获得输入的分数
2.将分数从字符串类型转换成数字类型
3.根据分数分档
    3.1  90-100  A档
    3.2  80-90   B档
    3.3  70-80   C档
    3.4  60-70   D档
    3.5  60以下  E档
"""

#获得用户输入分数
score = int(input('请输入分数：'))

# if score >= 90 and score <= 100:
#     print('太棒了！')
# elif score >= 80 and score < 90:
#     print('优秀！')
# elif score >= 70 and score < 80:
#     print('良好！')
# elif score >= 60 and score < 70:
#     print('及格！')
# elif score > 100 or score < 0:
#     print('输入错误！')
# else:
#     print('你完了！')

if score >= 0 and score <= 100:

    if score >= 90 and score <= 100:
        print('太棒了！')
    elif score >= 80 and score < 90:
        print('优秀！')
    elif score >= 70 and score < 80:
        print('良好！')
    elif score >= 60 and score < 70:
        print('及格！')
    else:
        print('你完了！')
else:
    print('输入错误！')

