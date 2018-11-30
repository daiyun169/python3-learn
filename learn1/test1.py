import sys
import os

# a = b = c = d = 20

# f, g, h = 1, 2, 3

# print('test', f, g, h)

# utterance = input('prompt: 请说话。。。')
# print('这是你说的话：', utterance)

# print(a, b, c, sep='||', end='$$')

# print(2 ** 4)

# print((a >= 100) and (a <= 200))

# print(100 <= a <= 200)

# y = int(input('请输入一个年份：'))
# print(((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0))

# list = ['李白','杜甫', '白居易','欧阳修']
# print('白居易' in list)
# print('klsajdlf' in list)
# str = 'wo shi zhong 国人'
# print('wo' in str)
#
# print(4<<2<<2)

# if 'admin' == input('ddd'):
#    print('admin')
# elif 'aaa' == 'dd':
#    print('aaa')
# count = 0
# while count < 10:
#     count = count + 1
#     print(count)
# else:
#     print('end')

# s = 'i love you more than i can say'
# for i in s:
#     print(i)
#
# for i, v in enumerate(s):
#     print(i, v)
#
# d = {'a': 'apple', 'b': 'banana', 'c': 'car', 'd': 'desk'}
#
# for key in d:
#     print(key, d.get(key))
#
# for k, v in d.items():
#     print(k, v, sep='=')
#
# for k, v in dict.items(d):
#     print(k, v, sep='-')

# 列表生成式
# l = range(10)
# print(list(l))
#
# print(range(0,10))
#
# for i in range(10):
#     print(i)
#
# lt = list(range(1,11))
# print(lt)

# l1 = [i for i in range(1, 11)]
# print(l1)
#
# l2 = [i * 2 for i in range(1, 11)]
# print(l2)
#
# l3 = [i * i for i in range(1, 11)]
# print(l3)
#
# l4 = [str(i) for i in range(1, 11)]
# print(l4)
#
# l5 = [i for i in range(1, 11) if i % 2 == 0]
# print(l5)
#
# l6 = ['你好啊：{num}'.format(num=num) for num in range(1, 11)]
# print(l6)
#
# print("{}-{}-{}-{}".format(1, 2, 3, 4))
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}'.format(j, i, j * i))
#     print()
#
# n = int(input('please input num:'))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# l = list(range(10))
# print(len(l))

# lt = [
#     {'name': '小王', 'age': 18, 'info': [('phone', '123'), ('dizhi', '广州')]},
#     {'name': '小芳', 'age': 19, 'info': [('phone', '789'), ('dizhi', '深圳')]},
#     {'name': '小杜', 'age': 22, 'info': [('phone', '567'), ('dizhi', '北京')]},
#     {'name': '小孟', 'age': 28, 'info': [('phone', '000'), ('dizhi', '上海')]},
#     {'name': '小乔', 'age': 26, 'info': [('phone', '111'), ('dizhi', '河南')]},
# ]
#
# for k in lt:
#     print('我叫{}，今年{}岁，我来自{}'.format(k['name'], k['age'], k['info'][1][1]))
#
#
# def say_hi(name):
#     print('hi,', name)
#
#
# say_hi('dairong')
#
#
# def add(a, b):
#     return a + b
#
#
# print(add(1, 1))
#
#
# def show(a, b='默认值'):
#     print(a)
#     print(b)
#
# show('a')
# show(1, 2)

#
# def var_len_args(a, b, name='default', *args, **kwargs):
#     print('a,b', a, b)
#     print('name', name)
#     print('args', args)
#     print('kwargs', kwargs)
#
#
# var_len_args(1, 2, 4, ab=18)
#
#
# def show(a, b):
#     print(a, b)
#
#
# l = (1, 2)
#
# show(l[0], l[1])
# show(*l)
#
#
# def show2(a='aa', b='bb'):
#     print(a, b)
#
#
# d = {'a': 'apple', 'b': 'banana'}
# show2(d['a'], d['b'])
# show2(**d)
#
# print(type(set([1,2])))
#
# print(abs(-10))
#
# print(chr(100))
#
# print(id('dairong'))
#
# print(max(1,2,3,45,6,))
#
# print(hex(10),oct(10),bin(10))

import random
import time
import math
import sys
import os

# print(random.randint(1, 10))
# print(random.randrange(100))
# print(random.uniform(1, 10))
# print(random.choice('wo ai ni zhong guo'))
# print(random.sample('wo ai ni zhong guo', 5))
# print(random.sample(range(10000000), 10))
# print(random.choices([1, 3, 2, 5]))
# print('time sleep', '2s')
# time.sleep(2)
# print('wake up')
# print(math.e)
# print(sys.argv)

# l = ['泉眼无声溪细流', '树阴照水爱晴柔', '小荷才楼尖尖角', '早有蜻蜓立上头']
# print(','.join(l))
#
# print('#'.ljust(3, 'p'))
# print('#'.rjust(3, 'a'))
# print('#'.center(7, 'l'))
# print('#'.zfill(5))
#
# print(l[0].replace('眼', 'yan', 10))
# print(l[1].find('水'))
# print(l[1].find('shui'))
# print(l[1].rfind('水'))
#
# print('abc'.upper())
# print('abc'.upper().lower())
# print('AbCdEfG'.swapcase())
# print('order by asc'.capitalize())
print('order by asc'.title())
#
# print('小荷才楼尖尖角'.count('尖'))
#
# print('富强民主和谐正直'.startswith('富强'))
# print('富强民主和谐正直'.startswith('强'))
# print('富强民主和谐正直'.endswith('正直'))
# print('富强民主和谐正直'.endswith('正'))
#
# print('富强民主和谐正直'.istitle())
# print('富强民主和谐正直'.islower())
# print('富强民主和谐正直'.isupper())
# print('富强民主和谐正直'.isdecimal())
#
# print('abc123'.isalpha())
# print('abc123'.isalnum())

l = ['泉眼无声溪细流', '树阴照水爱晴柔', '小荷才楼尖尖角', '早有蜻蜓立上头']

# l.append('小池')
# print(l)
#
# l.remove('小池')
# print(l)
#
# l.extend([i for i in range(10)])
# print(l)
#
# print(l.count('小荷才楼尖尖角'))
#
# print(l.index('小荷才楼尖尖角'))
#
# l.insert(0,'小池')
# print(l)
#
# print(l.pop())
# print(l)

# l.reverse()
# print(l)
#
# l.sort(reverse=True)
# print(l)
#
# s = [1, 2, 3, 4, 5, 6]
# s.sort(reverse=True)
# print(s)
#
#
# def sec(el):
#     return el[1]
#
#
# ss = [(4, 40), (8, 80), (3, 30), (10, 20)]
# ss.sort(key=sec, reverse=True)
# print(ss)
#
# s1 = ss
# print(id(ss.copy()), id(ss), id(s1))

# d = ['富强', '民主', '文明', '和谐', '自由', '平等', '公正', '法治', '爱国', '敬业', '诚信', '友善']
# dd = {}
# for i in d:
#     dd.update({str(d.index(i) + 1): i})
# print(dd)
#
# for k, v in dd.items():
#     print(k, v)
# print(dd.keys())
# print(dd.values())
# dd.pop('1')
# dd.popitem()
# print(dd)
# dc = dd.copy()
# dd.update({'1':'富强'})
# print(dd)
# print(dc)

s = {'富强', '民主', '文明', '和谐', '自由', '平等', '公正', '法治', '爱国', '敬业', '诚信', '友善'}
s.add('中国人')
print(s)

s.update(['a', 'b'])
print(s)

s.remove('a')
s.discard('')
print(s)

print(s.pop())
print(s)

print(s.issubset({'富强'}))
print(s.issuperset({'富强'}))
print(s.isdisjoint({'d'}))
