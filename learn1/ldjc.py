# class Animal:
#     def run(self):
#         print('1')
#
#     def eat(self):
#         print('2')
#
#
# class Cat(Animal):
#     def run(self):
#         print('3')
#
#     def eat(self):
#         super(Cat, self).eat()
#         print('4')


# jiafei = Cat()
# jiafei.run()
# jiafei.eat()
#
#
# class A:
#     def eat(self):
#         print('a')
#
#
# class B:
#     def eat(self):
#         print('b')
#
#
# class C(B, A):
#     def eat(self):
#         # A.eat(self)
#         # B.eat(self)
#         super().eat()
#
#
# c = C()
# c.eat()


class Person:

    def __setattr__(self, key, value):
        print(key, value)
        self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'age':
            return 123
        else:
            return 'default'

    def __delattr__(self, item):
        print('del', item)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __delitem__(self, key):
        del self.__dict__[key]


xiaoming = Person()
xiaoming.name = '小明'
xiaoming.age = 100
print(xiaoming.__dict__)

xiaoming['address'] = '湖南长沙'
print(xiaoming['address'])

print(xiaoming.address)
print(xiaoming.dict)

del xiaoming['address']
print(xiaoming.__dict__)


