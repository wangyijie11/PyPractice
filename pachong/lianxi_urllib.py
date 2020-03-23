import urllib.request
import urllib.error
import urllib.response
import urllib.parse
import urllib.robotparser

request = urllib.request.Request("http://www.gisquest.com/")
response = urllib.request.urlopen(request)
print(response.read())
