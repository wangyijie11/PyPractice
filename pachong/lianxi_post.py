import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser
import ssl

values = {"account": "wangyj", "password": "9217adSEFT"}
data = urllib.parse.urlencode(values).encode("utf-8")
url = "http://192.168.20.95:8000/login/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
           "Referer": "http://192.168.20.95:8000/login/",
           }

request = urllib.request.Request(url, data=data, headers=headers, origin_req_host="192.168.20.57", method='POST')

try:
    response = urllib.request.urlopen(request)
    print(response.read().decode("utf-8"))
except urllib.error.HTTPError as ex:
    print(ex)
except urllib.error.URLError as ex:
    print(ex)
else:
    print("ok")
