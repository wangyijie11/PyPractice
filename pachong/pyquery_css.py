from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')
print("addClass==========>", "\n", p.add_class("toto"))
print("removeClass==========>", "\n", p.remove_class("hello"))
print("toggle_class==========>", "\n", p.toggle_class("titi toto"))

print("css==========>", "\n", p.css("font-size", "15px"))
print(p.attr("style"))

print("=============>")
q = pq('<div><li></li></div>')
print(q.height("100"))
print(q.width("100"))
