#list = ['a', 'b']

list =['-'] * 30

print(list)
print(list[1])
list[1] = 'c'
print(list)
print(type(list))


x = ','.join(map(str, list))
print(type(x))
