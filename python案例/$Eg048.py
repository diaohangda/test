"""
    实例091：time模块
    题目 时间函数

"""

import time
import random

if __name__ == '__main__':
        start = time.clock()
        for i in range(100):
            print(i)
        end = time.clock()
        print('different is %6.3f' % (end - start))
