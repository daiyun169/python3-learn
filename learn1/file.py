# import os
# from os import path


# print(os.system('cls'))
# print(os.name)
# print(os.environ)
#
# print(os.getcwd())

# os.mkdir('hello')
# os.makedirs('hello/a/b')

# os.rmdir('hello')

# os.rename('hello', 'hi')
# print(os.stat('file.py').st_mode)
# print(os.listdir())

# print(path.join('/abc/def', '123'))
# name, ext = path.splitext('123/123/nihao.py')
# s = '123/456/789/10.py'
# print(name, ext)
# print(path.dirname(s))
# print(path.basename(s))
# print(path.exists('10.py'))
# print(path.isdir('hello'))
# print(path.isfile('file.py'))
# print(path.getsize('file.py'))

# 文件管理
# fp = open('G:/IMG/1.txt', 'r+')
# fp.write('hello world')
# print(fp.readable())
# print(fp.writable())
# print(fp.readlines())
#
# print(fp.tell())
# print(fp.seek(0, 0))
# print('123', fp.tell())
# fp.write('123')
# fp.close()
# os.remove('G:/IMG/1.txt')

# def removeDir(p):
#     dir = []
#     if path.isdir(p):
#         rl = os.listdir(p)
#         if len(rl) == 0:
#             print('删除：{}'.format(p))
#             os.removedirs(p)
#             return
#         dir.append(p)
#         for i in rl:
#             t = path.join(p, i)
#             if path.isfile(t):
#                 print('删除：{}'.format(t))
#                 os.remove(t)
#             elif path.isdir(t):
#                 if len(t) == 0:
#                     # 子文件夹是空文件夹
#                     print('删除：{}'.format(t))
#                     os.rmdir(t)
#                 else:
#                     dir.append(p)
#                     removeDir(t)
#         for i in dir:
#             if path.isdir(i):
#                 print('删除：{}'.format(i))
#                 os.rmdir(i)


# rm = 'G://IMG'


# print('需要删除的目录：{}'.format(os.listdir(rm)))
# removeDir(rm)

# def rdir(p):
#     for root, dirs, files in os.walk(p, topdown=False):
#         print('root : {}'.format(root), 'dirs : {}'.format(dirs), 'files : {}'.format(files), sep='\n')
#         for name in files:
#             os.remove(path.join(root, name))
#         for name in dirs:
#             os.rmdir(path.join(root, name))
#     os.rmdir(p)


# rdir(rm)
# rdir('G:/download-mzitu')

# import shutil
#
# shutil.rmtree(rm)

import os


def copy(src, dst):
    # print('拷贝开始: {} ==》 {}'.format(os.path.abspath(src), os.path.abspath(dst)))
    if not os.path.exists(src) or not os.path.isfile(src):
        print('源文件不存在或者不是有效的文件，无法拷贝')
        return
    if os.path.abspath(src) == os.path.abspath(dst):
        print('源文件与目标地址相同，无法拷贝')
        return

    src_fp = open(src, 'r')
    dst_fp = open(dst, 'w')
    content = src_fp.read(1024)
    while len(content):
        dst_fp.write(content)
        content = src_fp.read(1024)
    src_fp.close()
    dst_fp.close()


s = 'G:/img/10.txt'
d = 'G:/img/20.txt'
copy(s, d)


def remove(file):
    if not os.path.exists(file):
        print('文件不存在，无法删除')
        return
    if os.path.isfile(file):
        os.remove(file)
        return
    dirs = os.listdir(file)
    for f in dirs:
        file_name = os.path.join(file, f)
        if os.path.isfile(file_name):
            os.remove(file_name)
        else:
            remove(file_name)
    os.rmdir(file)


remove('G:/gank.io')


def size(file):
    if not os.path.exists(file):
        print('文件不存在，无法计算大小')
        return
    if os.path.isfile(file):
        return os.path.getsize(file)
    total = 0
    dirs = os.listdir(file)
    for f in dirs:
        file_name = os.path.join(file, f)
        if os.path.isfile(file_name):
            total += os.path.getsize(file_name)
        else:
            total += size(file_name)
    return total


print(size('G:\elasticsearch-6.4.0')/1024/1024)
