from lxml import etree

html = etree.parse('index.html')

# 获取所有<li>标签
result1 = html.xpath('//li')
print("获取所有<li>标签")
print(result1)
print(type(result1), "\n")

# 获取<li>标签的所有class
result2 = html.xpath('//li/@class')
print("获取<li>标签的所有class")
print(result2)
print(type(result2), "\n")

# 获取<li>标签下href为link1.html的<a>标签
result3 = html.xpath('//li/a[@href="link1.html"]')
print("获取<li>标签下href为link1.html的<a>标签")
print(result3)
print(type(result3), "\n")

# 获取<li>标签下所有<span>标签
result4 = html.xpath('//li//span')
print("获取<li>标签下所有<span>标签")
print(result4)
print(type(result4), "\n")

# 获取<li>标签下所有class，不包括<li>
result5 = html.xpath("//li/a//@class")
print("获取<li>标签下所有class，不包括<li>")
print(result5)
print(type(result5), "\n")

# 获取最后一个<li>的<a>的href
result6 = html.xpath("//li[last()]/a/@href")
print("获取最后一个<li>的<a>的href")
print(result6)
print(type(result6), "\n")

# 获取倒数第二个元素的内容
result7 = html.xpath("//li[last()-1]/a")
print("获取倒数第二个元素的内容")
print(result7)
print(type(result7), "\n")

# 获取class为bold的标签名
result8 = html.xpath('//*[@class="bold"]')
print("获取class为bold的标签名")
print(result8)
print(type(result8), "\n")