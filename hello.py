#!/usr/bin/python3

import sys
from my_package.test import print_func

# -------演示导入module中的function--------
print_func('zmrdlb')

# --------演示读取命令行参数----------
# print('命令行参数如下：')

# input: python3 ./hello.py argv1 argv2
# output: ./hello.py argv1 argv2
# for i in sys.argv:
#     print(i)
#
# print('Python 路径为：', sys.path)

# --------演示了如何实现多行语句--------
# print("Hello," + \
#     " World!")
