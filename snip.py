list = ["snippets"]
print(list[0])
print(list[2:])
print(len(list))

list.append('java')
print(list)

list.insert(1,'c')
print(list)

list.remove('c')
print(list)

list.sort()
print(list)

tuple = ("snippets")
print(tuple[2:4])
print(tuple)

dict = {"snippets":'snippets',"flower":'water'}
del dict["flower"]
print(dict)
