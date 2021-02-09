from tkinter import Tk
from urllib import request, parse

result = Tk().clipboard_get()
url = 'https://clipboard.ziiimo.cn:66/send'
print(result)
params = {'secret': '688cdcff00dd183', 'clipboard': result}
data = bytes(parse.urlencode(params), encoding='utf8')
response = request.urlopen(url, data=data)
result = response.read().decode('utf-8')
print(result)