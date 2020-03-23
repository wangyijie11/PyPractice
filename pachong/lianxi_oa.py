import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser
import ssl
import http.cookiejar



values = {"loginid": "wangyj", "userpassword": "wangyj123"}
data = urllib.parse.urlencode(values).encode("utf-8")
url = "http://192.168.11.71:9083/login/Login.jsp?logintype=1"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
           }
request = urllib.request.Request(url, data=data, headers=headers, origin_req_host="192.168.20.57", method='POST')

# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)


try:
    response = opener.open(request)
    for item in cookie:
        print(item.name+"="+item.value)
except urllib.error.HTTPError as ex:
    print(ex)
except urllib.error.URLError as ex:
    print(ex)
else:
    print("ok")
