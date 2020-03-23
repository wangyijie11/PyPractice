from pyquery import PyQuery as pq

d = pq('<p id="hello" class="hello"><a/></p><p id="test"><a/></p>')

print(d('p').filter('.hello'), '\n')
print(d('p').eq(1), "\n")
print(d('p').find('a'),"\n")
print(d('p').find('a').end(), "\n")
