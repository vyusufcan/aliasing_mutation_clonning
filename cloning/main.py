a = [1,2,3,4,5]

b = a # alias

b[0] = 15

print(a)
print(b)

my_list = [1,2,3,4,5]

copy_list = my_list[:] # copy object
copy_list[0] = 15

print(my_list)
print(copy_list)


def remove_even_values(dictionary):
    #for key, value in dictionary.items(): # gives error
     for key, value in dictionary.copy().items():
        if value % 2 == 0:
            del dictionary[key]


my_dictionary = {"a": 1, "b": 2}

remove_even_values(my_dictionary)
print(my_dictionary)