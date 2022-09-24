"""
    实例025：阶乘求和
    题目 求1+2!+3!+…+20!的和。

    程序分析 1+2!+3!+…+20!=1+2(1+3(1+4(…20(1))))
"""

res=1
for i in range(20,1,-1):
    res=i*res+1
print(res)

# import math
# sum=0
# for i in range(1,21):
#    sum+=math.factorial(i)
# print(sum)

# def factorial(n):
#     return n * factorial(n - 1) if n > 1 else 1
# sum=0
# for i in range(1,21):
#     sum+=factorial(i)
# print(sum)