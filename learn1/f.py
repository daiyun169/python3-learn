import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


path = 'F:\\text.txt'
# p1 = Person('赵子龙', 100);
# fp = open(path, 'wb')
# pickle.dump(p1, fp)
# print('存储完毕')


fp2 = open(path, 'rb')
d = pickle.load(fp2)
print(d.name)
print(d.age)


fp2.close()