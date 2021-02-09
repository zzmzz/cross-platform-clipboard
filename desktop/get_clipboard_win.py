from urllib import request, parse
import os
url = 'https://clipboard.ziiimo.cn:66/get'
params = {'secret': '688cdcff00dd183'}

data = bytes(parse.urlencode(params), encoding='utf8')
response = request.urlopen(url, data=data)
result = response.read().decode('utf-8')

print(result)

file_handle=open('tmp',mode='w')
file_handle.write(result)
file_handle.close()
command = 'type tmp| clip'
os.system(command)