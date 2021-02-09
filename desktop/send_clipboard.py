from tkinter import Tk
import requests

result = Tk().clipboard_get()
url = 'https://clipboard.ziiimo.cn:66/send'
print(result)
myobj = {'secret': 'zzm_secret', 'clipboard': result}
x = requests.post(url, data=myobj)
print(x)