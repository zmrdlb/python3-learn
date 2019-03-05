#!/usr/bin/python3

class Animal:
    """
    这是一个基本的Animal class。

    此class用来说明python的class用法。

    类变量：
        定义在class中切在函数体之外，在整个实例化对象中是公用的。通常不作为实例变量使用。
        可以通过类或者实例的方式来访问。

        example:
            定义类变量 queue = []

            >>> dog = Animal('dog')
            >>> cat = Animal('cat')
            >>> print(dog.queue,cat.queue,Animal.queue)
            [] [] []
            >>> # 实例dog,cat和类的queue都是访问的类变量queue
            >>> cat.queue.append('lovely_animal')
            >>> print(dog.queue,cat.queue,Animal.queue)
            ['lovely_animal'] ['lovely_animal'] ['lovely_animal']
            >>> # cat操作了类变量queue，所以影响了整个类变量
            >>> cat.queue = ['cat_more_lovely']
            >>> print(dog.queue,cat.queue,Animal.queue)
            ['lovely_animal'] ['cat_more_lovely'] ['lovely_animal']
            >>> # cat重新定义了queue，分配新值到堆heap里，引用指针到栈stack里。
            此时cat.queue指向实例属性而不是类变量。而dog.queue还是指向类变量Animal.queue

    实例变量：
        通过self.定义的都是实例变量
    """

    # 类变量

    # 两个下划线开头为私有属性, 在类外部无法直接访问
    __animal_count = 0

    def __init__(self, name):

        # 可以直接给self赋值属性，而不用事先定义。
        self.name = name

        Animal.__animal_count += 1

    def animal_count(self):
        return Animal.__animal_count;

class Mammal(Animal):
    """哺乳动物类"""

    __category = "a mammal"

    def __init__(self, name):

        # 用super调用父类指定方法
        super(Animal, self).__init__(name)

    def category(self):
        return self.__category
