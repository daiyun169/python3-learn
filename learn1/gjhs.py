l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def double(x):
    return 2 * x


m = map(double, l)
print(list(m))

m1 = map(lambda x: x * x, l)
print(list(m1))

# 练习
s = ['dairong  ', ' shi ', 'ge', 'chengxuyuan ']
# rs = map(lambda s: str(s).replace(' ', '').capitalize().title(), s)
rs = map(lambda s: str(s).strip().capitalize().title(), s)
print(s, list(rs), sep=' => ')

from functools import reduce

print('reduce sum :', reduce(lambda x, y: x + y, l))
print('reduce result :', reduce(lambda x, y: x * 10 + y, l))
print('reduce result :', reduce(lambda x, y: x * y, l))

f = filter(lambda x: x % 2 == 0, l)
print(l)
print(list(f))

print('奇数并且能被3整除：', list(filter(lambda x: x % 2 != 0 and x % 3 == 0, l)))

a = [2, 5, 9, 1, 6, 3]
ra = sorted(a, reverse=True)
print(ra)

ao = [
    {'name': 'xiaowang', 'age': 18, 'height': 150},
    {'name': 'xiaogang', 'age': 20, 'height': 140},
    {'name': 'xiaohong', 'age': 19, 'height': 145},
]

aor = sorted(ao, key=lambda x:x['age'])
print(aor)