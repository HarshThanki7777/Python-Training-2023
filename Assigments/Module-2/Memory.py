'''
Memory management in Python is handled automatically by the Python memory manager. The memory manager is responsible for allocating and deallocating memory
for objects and data structures in your program, so you don’t have to worry about it. Python has a private heap that stores all of the program’s 
objects and data structures

Python uses reference counting and garbage collection to manage memory.
Reference counting works by counting the number of references to an object. 
When an object’s reference count drops to zero, it is no longer accessible and can be deallocated1. Garbage collection is used to find and
deallocate objects that are no longer accessible 
but still have a non-zero reference count due to reference cycles
'''

import sys 

x = object()
print(sys.getrefcount(x))

y = x 
print(sys.getrefcount(x))

del y 
print(sys.getrefcount)