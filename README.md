# aliasing_mutation_clonning
# Alias
Used to indicate an additional name that a person sometimes uses
# Alias in Programming
Two or more references to the same memory address in the program
Different Name , Same Object
# Mutability and Immutability
# Mutation
Change - a significant and basic alteration

Object:
    - Mutable --> Can be modified (lists, sets, dictionaries)
    - Immutable --> Can't be modified ( Booleans, Integers, Floats, Strings, Tuples)
# Advantages of Mutable Objects

*Memory Efficiency*
Reuse existing objects instead of making new copies for each change

*Reald-World Objects*
Represent real-world objects that are mutable by nature

# Disadvantages of mutable objects

*Bugs*
Using mutable objects in a program might introduce bug
You might unintentionally mutate an object in the program

# Potential Risks of Aliasing

*Mutating Objects*
We might mutate an object unintentionally through an alias

```python
a = [1, 2, 3, 4]
b = a

b[0] = 15
print(b)
print(a)
```
# Advantages of Immutable Objects

*Safer from bugs*
Since they can't be modified, they are less likely to introduce bugs

*Easier to Understance*
Know their exact value, without any "hidden" or unexpected changes
# Disadvantages of Immutable Objects

*Less Efficient*
You need to create a new copy of the object to make any changes, which can be costly

```python
a = (1, 2, 3, 4)
print(id(a))

a = a[:2] + (7,) + a[2:]
print(id(a))
```

# Cloning in Python

*Cloning*
Creating an exact copy of the object that is completely independent from the original object
Opposite of the alliasing

*Shallow Copy*
When you make a shallow copy of an object, you are making a new object in memory, a new reference, but the content
of the object will still point the same objects

*Deep Copy*
With a deep copy, in addition to creating a copy of the "container" object, you also create a copy of the elements contained in the object

# Clone Tuples Have the Same id - Why?
Tuples are immutable in Python, which means that they cannot be modified. Once you define a tuple, you cannot change the elements that contained directly within the tuple.
This is why Python doesn't create a new tuple when you try to clona a tuple.
Instead, it assigns a reference to the original tuple in memory
This optimizes memory usage