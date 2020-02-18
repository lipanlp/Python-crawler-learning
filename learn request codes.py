import urllib.request
import urllib.error
rep=urllib.request.urlopen("http://python.org/")
res=rep.read().decode('utf-8')
print(res)

#def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile = None, capath = None,cadefault = False, context = None):
    #data：是我们要发给服务器请求的额外信息（比如登录网页需要主动填写的用户信息）。如果需要添加data参数，那么是POST请求，默认无data参数时，就是GET请求；

    #一般来讲，data参数只有在http协议下请求才有意义
    #data参数被规定为byte
    #object，也就是字节对象
    #data参数应该使用标准的结构，这个需要使用urllib.parse.urlencode()
    #将data进行
    #转换，而一般我们把data设置成字典格式再进行转换即可；data在以后实战中会介绍如何使用

    #timeout：是选填的内容，定义超时时间，单位是秒，防止请求时间过长，不填就是默认的时间；
    #cafile：是指向单独文件的，包含了一系列的CA认证 （很少使用，默认即可）;
    #capath：是指向文档目标，也是用于CA认证（很少使用，默认即可）；
    #context：设置SSL加密传输（很少使用，默认即可）；

print(rep.geturl())  #返回URL，用于看是否有重定向。
#>>>https://www.python.org/
print(rep.info())#返回元信息，例如HTTP的headers。
print(rep.getcode())#返回回复的HTTP状态码，成功是200，失败可能是503等，可以用来检查代理IP的可使用性。

#很多网站都有反爬机制，因此需要在request的时候提交header，其中的user-agent:就非常有用了
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
rep=urllib.request.Request('http://python.org/', headers=headers)
html=urllib.request.urlopen(rep)
res=html.read().decode('utf-8')
print(res)

try:

    response = urllib.request.Request('http://python.org/',
                                       headers=headers)
    html = urllib.request.urlopen(response)
    result = html.read().decode('utf-8')
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误状态码是' + str(e.code))
else:
    print('请求成功通过。')