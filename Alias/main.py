a = [1, 2, 3, 4]

b = a  # alias
c = b
d = c

print(a is b)
print(a is b is c is d)

print(id(a))
print(id(b))
print(id(c))
print(id(d))
