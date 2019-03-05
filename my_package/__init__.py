"""
测试 package

对于引入package的总结：

    使用如下方式导入：from my_package import *
    如果不定义__all__, 则只导入my_name。前面有_的变量不会被导入
    如果定义了__all__，则只导入__all__里定义的module。此处是test

"""

_my_age = 29
my_name = 'zmrdlb'

__all__ = ['test']
