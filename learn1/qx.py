# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def eat(self):
#         print('民以食为天')
#
#     def __inner(self):
#         print('私有方法，不想让外部调用')
#
#     def test(self):
#         print(self.__age)
#         self.__inner()
#
#
# p = Person('赵子龙', 100)
#
# p.eat()
# print(p.name)
#
# # print(p._Person__age)
# # p._Person__inner()
#
# p.test()
#
#
# class Man(Person):
#     def test(self):
#         print('子类无法使用父类的私有属性和方法')
#
#
# m = Man('mugai', 50)
# m.test()

class Pig:
    nation = 'zhongguo'

    def __init__(self):
        print('大师兄，我快不行了')

    @classmethod
    def create(cls):
        p = cls()
        p.age = 1
        return p

    @staticmethod
    def halou():
        print('halou')


pig = Pig()

del pig

print('一路好走')

print(Pig.__name__)
print(Pig.__bases__)


p = Pig.create()
print(p.age)

Pig.halou()
