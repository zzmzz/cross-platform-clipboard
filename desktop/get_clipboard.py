from tkinter import Tk
import requests

url = 'https://clipboard.ziiimo.cn:66/get'
myobj = {'secret': 'zzm_secret'}
x = requests.post(url, data=myobj)
tk=Tk()
tk.clipboard_clear()
tk.clipboard_append(x.text)
tk.after(500, tk.destroy)
tk.mainloop()