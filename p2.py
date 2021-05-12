phrase = "!salam Va vaght bekheyr !"
ph_list = list(phrase)
for i in range(2):
    ph_list.pop()
ph_list.pop(0)
ph_list.remove(" ")
ph_list.remove("V")
print(ph_list)
ph_list.insert(2, ph_list.pop(15))
ph_list.insert(3, ph_list.pop(16))
ph_list.insert(4, ph_list.pop(13))
ph_list.remove("l")
ph_list.insert(6, ph_list.pop())
for i in range(12):
    ph_list.pop()

print(ph_list)
new_phrase = "".join(ph_list)
print(new_phrase)
