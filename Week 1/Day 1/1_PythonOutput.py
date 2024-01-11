"""
1. Python Output
print(value, .., sep=' ', end='\n', file=sys.stdout, flush=False)
Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end:
string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
"""

print("Hello World!")
print("Salman Khan")

print(7)
print(7.7)

print(True)

print("Hello",1.4,1,True)

#Working With Inner attributes
print("Hello",1.4,1,True,sep = " -")

print("Hello",end='/')
print("World")