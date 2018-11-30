import inspect


def wait():
    def nei():
        print('内部函数')

    return nei


print(type(wait()) == int)
wait()()

print(inspect.isfunction(wait()))


def wai(n):
    def nei():
        return n * n

    return nei


f1 = wai(3)
f2 = wai(4)

print(f1)
print(f2())


def wai(*args):
    def nei():
        he = 0
        for i in args:
            he += i
        return he

    return nei


f1 = wai(1, 2, 3)
print('t', f1())


def wai(a, b):
    def nei(x):
        return a * x + b

    return nei


f1 = wai(3, 5)

print(f1(3))

f2 = wai(5, 8)

print(f2(6))
print(wai(2, 4)(4))
