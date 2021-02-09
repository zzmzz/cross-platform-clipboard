# cross-platform-clipboard

- 主要解决下windows和iOS设备间剪贴板不互通的痛点。
- 虽然市面上有一些类似的app，但支持ios的相对较少，且大多依赖安装的app，另外走公共服务器也有一定安全风险
- 该项目提供了iOS快捷指令+windows python脚本的方案

## 你需要什么
 - 一台服务器，为了保证数据安全，我也不直接提供公共服务器了，毕竟谁也不想自己的剪贴板被别人监视
 - 你需要觉得ios和windows间粘文字不想再打开微信qq这些东西。如果你觉得用微信qq来粘贴也还可以，那么你就可以退出去了

## 怎么做
 - **服务器部署**
     - 服务器可以拉取docker镜像
       - `  docker pull registry.cn-beijing.aliyuncs.com/zmzhu94/clipboard:latest`
     - 修改app.py中的secret，改成只有你知道的秘钥
     - 将app.py 放在一个目录下，下称your_source_dir
     - 服务器执行
       - ` docker run --name clipboard -v your_source_dir:/src -p 8080:8080 registry.cn-beijing.aliyuncs.com/zmzhu94/clipboard:latest `
     - 此时服务器就能启动8080端口用于接收剪贴板内容

 - **客户端**
     - 由于mac和ios原生支持互通剪贴板，这里就不单独支持了，这里只提供windows版本的脚本
     - 到python官网下载下python3的最新版本，安装时记得勾上将python加入path
     - desktop文件夹内，get_clipboard_win.py 是获取其他平台上传的剪贴板内容
     - send_clipboard.py是把本地剪贴板内容传给服务器
     - 记得改下url和secret
     - windows可以对脚本创建快捷方式，并添加快捷键，这里就不再赘述了

 - **iOS**
     - 发送剪贴板内容 `https://www.icloud.com/shortcuts/dc8b00e8834549b28ccf12acab0152dc`
     - 获取剪贴板内容 `https://www.icloud.com/shortcuts/bf8ec91e1a5a48acbb172d95900eaf37`
     - 也记得改下url和secret

## TODO
- 剪贴板互通文件，理论上也可以用快捷指令搞，后续做一下。目前用nas中转不算复杂，感觉可以用webDAV的方式减少操作步骤