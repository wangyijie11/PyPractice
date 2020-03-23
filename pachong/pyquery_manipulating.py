from pyquery import PyQuery as pq

d = pq('<p class="hello" id="hello">python rocks</p>')
# 加在原有内容的后面
d('p').append('<a href="http://reddit.com/r/python"><span>reddit</span></a>')
print(d, "\n")

p = d('p')
# 加在原有内容的前面
p.prepend('you know ')
print(p, "\n")

d = pq('<html><body><div id="test"><a href="http://python.org">python</a></div></body></html>')
p = pq('python rock')
# 指定位置
p.prepend_to(d("#test"))
print(d, "\n")

# 在test的后面插入
p.insert_after(d('#test'))
print(d, "\n")

# 在test的前面插入
p.insert_before(d('#test'))
print(d, "\n")


p = pq('<html><body><p id="id">Yeah!</p><p>python rocks !</p></div></html>')

# 删除指定元素
p.remove('p#id')
print(p, "\n")

# 指定元素的text内容为空
p('p').empty()
print(p, "\n")