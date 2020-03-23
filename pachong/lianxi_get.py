import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser

values={"username": "wangyijie11", "password": "wyj9217"}
data = urllib.parse.urlencode(values)
url = "https://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
