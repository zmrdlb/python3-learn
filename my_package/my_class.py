#!/usr/bin/python3

class Animal:
    """这是一个基本的Animal class"""

    # 定义基本属性。可以通过类或实例对象访问。
    #     类访问：只会读取到类定义时声明的值
    #     实例访问：每个实例都各自有一份，互不影响
    name = "an animal"

    # 两个下划线开头为私有属性, 在类外部无法直接访问
    __animal_count = ""

    def __init__(self, name):

        # 可以直接给self赋值属性，而不用事先定义。
        self.name = name

        self.__animal_count++;

    def animal_count(self):
        return self.__animal_count;

class Mammal(Animal):
    """哺乳动物类"""

    __category = "a mammal"

    def __init__(self, name):

        # 用super调用父类指定方法
        super(Animal, self).__init__(name)

    def category(self):
        return self.__category;
