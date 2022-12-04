a = [7, 3, 2, 1]
a[0] = 5
print(a)

a = (7, 3, 2, 1)
a[0] = 5 # gives error. Tuples are immutable

a = "Hello, World!"
a[0] = "S" # gives error. Strings are immutable