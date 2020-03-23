from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')('p')
print("attr============>")
print(p.attr("id"))
print(p.attr("id", "plop"))
print(p.attr("id", "hello"))
print(p.attr.id)
p.attr.id = "plop"
print(p.attr.id)
p.attr["id"] = "ola"
print(p.attr.id)
print(p.attr(id="hello", class_="hello2"))
p.attr.class_ = "hello"
print(p.attr.class_)

print("removeAttr==============>")
image = pq('<img src="test.jpg"/>')
print(image.remove_attr("src"))

print("addClass=============>")
li = pq('<ul><li>hello</li><li>hello</li></ul>')
print(li.add_class("li_demo"))
print(li.remove_class("li_demo"))

print("html===========>")
print(li.html())

print("text===========>")
print(li.text())

print("val===========>")
print(li.val("123"))
print(li.val())