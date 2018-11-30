# try:
#     print('123')
#     print(3 / 0)
# except ZeroDivisionError as e:
#     print('异常出现')
#     print(e)
# print('456')


# try:
#     print(a)
#     # print(3/0)
#     # fp = open('123.txt')
# except NameError as e:
#     print('name error', e)
# except ZeroDivisionError as e:
#     print('zero division error', e)
# except Exception as e:
#     print('other', e)

# try:
#     print('13')
#     print(3 / 0)
# except Exception as e:
#     print('yc', e)
# else:
#     print('zcjs')
# finally:
#     print('end')
#
# try:
#     print('start')
#     raise Exception('custom except')
#     print('123')
# except Exception as e:
#     print('chuxianyic', e)
#
# print('我要去上班，什么事情都不能阻止我上班的脚步')
# try:
#     print('我准备骑电动车')
#     raise Exception('昨天晚上那个缺德的家伙把我充电器给拔了，无法骑车')
#     print('骑电动车提前到达公司')
# except Exception as e:
#     print(e)
#     try:
#         print('我准备坐公交')
#         raise Exception('等了20分钟一直没有公交车，果断放弃')
#         print('坐公交准时到达公司')
#     except Exception as e:
#         print(e)
#         print('我准备打车')
#         print('打车还是快，一会就到公司了')
# print('热情满满的开始一天的工作')


# class MyException(Exception):
#
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
#
#     def deal(self):
#         print('异常已处理')
#
#
# try:
#     print('正常执行')
#     raise MyException('我自定义的异常类型')
# except MyException as e:
#     print(e.msg)
#     e.deal()

with open('G:\\elasticsearch-6.4.0.zip', 'rb') as fp:
        c = fp.read(5)
        print(c)










