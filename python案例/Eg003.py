"""
    实例003：完全平方数
    题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

    程序分析 因为168对于指数爆炸来说实在太小了，所以可以直接省略数学分析，用最朴素的方法来获取上限:
        n=0
        while (n+1)**2-n*n<=168:
             n+=1
        print(n+1)------85
"""
n=0
while (n+1)**2-n*n<=168:
    n+=1


for i in range((n+1)**2):
    if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5):
        print(i-100)

