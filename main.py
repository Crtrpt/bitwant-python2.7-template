# -*- coding: UTF-8 -*-
class class_a:
    def __init__(self):
        pass

    @staticmethod
    def func(a, b):
        # 交换b,a的值并且返回
        a, b = b, a
        return a, b


if __name__ == '__main__':
    class_a.func(1, 2)
