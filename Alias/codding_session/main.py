class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius
    

my_circle = Circle(4)
your_circle = my_circle

print(my_circle is your_circle)


print("Before:  ")
print(my_circle.radius)
print(your_circle.radius)


your_circle.radius = 18 # also changes the my_circle. Because reference to same object
print("After:   ")
print(my_circle.radius)
print(your_circle.radius)
