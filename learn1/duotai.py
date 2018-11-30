# class Animal:
#     def run(self):
#         pass
#
#
# class Dog(Animal):
#     def run(self):
#         print('狗奔跑的时候一般是s型')
#
#
# class Cat(Animal):
#     def run(self):
#         print('猫平时走猫步，偶尔会突然加速')
#
#
# def func(obj):
#     obj.run()
#
#
# func(Dog())
# func(Cat())

from inspect import isfunction


class User:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return '有人想直接获取密码，没门'

    @password.setter
    def password(self, password):
        print('注意了，有人想修改密码')
        self.__password = 'xxx' + password + 'yyyy'


u = User('xiaoming', '123456')

print(u.username)

print(u.password)

u.password = '654321'


class Person:

    def __call__(self, *args, **kwargs):
        return sum(args)


def test():
    pass


p = Person()

ret = p(1, 2, 3, 4, 5, 6, 7, 8, 9, name='dairong')
print(ret)

print(callable(p))
print(callable(test))

print(hasattr(test, 'call'))
print(hasattr(p, '__call__'))
print(hasattr(u, 'username'))

print(isfunction(test))
print(isfunction(u))
print(isfunction(p))
