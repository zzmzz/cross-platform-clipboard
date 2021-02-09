from tkinter import Tk
import requests

result = Tk().clipboard_get()
url = 'https://yourhost:66/send'
print(result)
myobj = {'secret': 'zzm_secret', 'clipboard': result}
x = requests.post(url, data=myobj)
print(x)