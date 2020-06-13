import urllib.request
import urllib.error
import urllib.parse
import ssl
import re

page = 1
url = "https://www.qiushibaike.com/"
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
context = ssl._create_unverified_context()
try:

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request, context=context)
    content = response.read().decode()
    pattern = re.compile('<div class="dataRight">.*?<h3 class="ellipsis">(.*?)</h3>' +
                         '.*?<font.*?>(.*?)</font>' +
                         '.*?<p>(.*?)</p>.*?<p class="introduce">(.*?)</p>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print(item[0], item[1], item[2], item[3])
except urllib.error.URLError as ex:
    print(ex)
