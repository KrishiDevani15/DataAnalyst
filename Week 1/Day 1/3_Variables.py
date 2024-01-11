"""
3. Variables

Static Vs Dynamic Typing
Static Vs Dynamic Binding
stylish declaration techniques
"""

# C/C++
name = 'Krishi'
print(name)

a = 5
b = 6

print(a + b)


# Dynamic Typing :- No need to declare the DataType eg Python
a = 5
# Static Typing :- need to declare the DataType eg C++,C,Java
# int a = 5


# Dynamic Binding :- Dynamically change its datatype and stored accordingly
a = 5
print(a)
a = 'Krishi'
print(a)

# Static Binding :- In this only declared variable values are stored eg int a = int value
# int a = 5


a = 1
b = 2
c = 3
print(a,b,c)

a=b=c= 5
print(a,b,c)