import re

# m = re.match('abc', 'abcdlsabcjdf')

m = re.search('abc', 'helloabcasdfabc')

if m:
    print('ok')
    print(m.group())
    print(m.span())

f = re.findall('abc', 'abclsdfjlabclskdjflkabcsdkjflkabc')

if f:
    print(f)
