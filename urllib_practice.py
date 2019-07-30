# import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# ----------------------------------------------------------
# import urllib.parse
# import urllib.request

# string = urllib.parse.urlencode({'word': 'hello'})
# data = bytes(string, encoding='utf=8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
# ------------------------------------------------------------
# import socket
# import urllib.request
# import urllib.error

# try:
# 	response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
# 	if isinstance(e.reason, socket.timeout):
# 		print('TIME OUT!')
# -----------------------------------------------------
# from urllib import request, parse

# url = 'http://httpbin.org/post'
# headers = {
# 	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
# 	'Host': 'httpbin.org'
# }
# dict = {
# 	'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf8'))
# --------------------------------------------------------------

# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError

# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
# 	result = opener.open(url)
# 	html = result.read().decode('utf-8')
# 	print(html)
# except URLError as e:
# 	print(e.reason)
# ---------------------------验证-----------------------------------

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener

# proxy_handler = ProxyHandler({
# 	'http': 'http://127.0.0.1:9743',
# 	'https': 'https://127.0.0.1:9743'
# 	})
# opener = build_opener(proxy_handler)
# try:
# 	response = opener.open('https://www.baidu.com')
# 	print(response.read().decode('utf8'))
# except URLError as e:
# 	print(e.reason)
# ---------------------------代理----------------------------

# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print(item.name+"="+item.value)

# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# hanlder = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(hanlder)
# reponse = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# --------------------------Cookies--------------------------

# from urllib import request, error
# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
# 	print(e.reason)
# --------------------------异常处理：URLError--------------------------

# from urllib import request,error
# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
# 	print(e.reason, e.code, e.headers, sep='\n')
# --------------------------异常处理：HTTPError--------------------------

# from urllib import request, error

# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
# 	print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
# 	print(e.reason)
# else:
# 	print('Request Successfully')
# --------------------------异常处理：HTTPError是URLError的子类，先捕获子类异常--------------------------

from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
# --------------------------URL解析--------------------------
