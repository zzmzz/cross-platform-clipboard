from tkinter import Tk
from urllib import request, parse

result = Tk().clipboard_get()
url = 'https://yourhost/send'
print(result)
params = {'secret': '63f369b84e1aec', 'clipboard': result}
data = bytes(parse.urlencode(params), encoding='utf8')
response = request.urlopen(url, data=data)
result = response.read().decode('utf-8')
print(result)