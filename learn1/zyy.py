if True:
    name = 'dairong'
print(name)


def test():
    a = 10


# print(a)

num = 10


def show():
    global num
    num = 30
    print(num)


show()
print(num)

print('=========')


def wai():
    age = 20

    def nei():
        # 使用外层函数的局部变量
        nonlocal age
        age = 30
        print('1',age)

    nei()
    print('2',age)


wai()
