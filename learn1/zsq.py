from collections import Iterator

def show():
    pass


print(show())


def shuai(func):
    def wrapper():
        print('前置处理')
        func()
        print('后置处理')

    return wrapper


@shuai
def mugai():
    print('妮胖胖是真的很胖')


mugai()


def zsq(func):
    def wrapper(*args, **kwargs):
        print('前置处理')
        func(*args, **kwargs)

    return wrapper


@zsq
def test(n):
    print('我的幸运数字是：{}'.format(n))


test(1)


def zhuanshiqi(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 10

    return wrapper


@zhuanshiqi
def pingfang(n):
    return n * n


print(pingfang(4))

# 列表生成式
l1 = [i for i in range(10)]
print(l1)

# 列表生成器
l2 = [i for i in range(10)]
l3 = (i for i in range(3))
print(type(l2), type(l3))
print(l2)
# print(list(l3))

# print(next(l3))
# print(next(l3))
# print(next(l3))
# print(next(l3))
# print(next(l3))

for i in l3:
    print('231', i)


def test(n):
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return l


print(test(5))


def test2(n):
    for i in range(10):
        yield i


t = test2(5)
print(list(t))

print(isinstance(test(1), Iterator))
print(isinstance(t, Iterator))

print(isinstance(iter(test(1)),Iterator))



