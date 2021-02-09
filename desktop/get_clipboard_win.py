from urllib import request, parse
import os
url = 'https://yourhost/get'
params = {'secret': 'your_key'}

data = bytes(parse.urlencode(params), encoding='utf8')
response = request.urlopen(url, data=data)
result = response.read().decode('utf-8')

print(result)

file_handle=open('tmp',mode='w')
file_handle.write(result)
file_handle.close()
command = 'type tmp| clip'
os.system(command)