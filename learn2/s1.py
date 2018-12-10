import requests

# response = requests.get('http://www.cnhnb.com/')
# content = response.content
# header = response.headers
# print(content)
# print(header)


data = {'data1':'','data2':''}
response = requests.post('http://www.cnhnb.com/')
print(response.content)