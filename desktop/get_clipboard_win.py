from urllib import request, parse
import os
url = 'https://yourhost/get'
params = {'secret': '63f369b84e1aec'}

data = bytes(parse.urlencode(params), encoding='utf8')
response = request.urlopen(url, data=data)
result = response.read().decode('utf-8')
command = 'echo ' + result.strip() + '| clip'
os.system(command)