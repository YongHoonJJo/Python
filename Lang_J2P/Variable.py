### About Variable ###

a = 3

# a is Reference that points at object(having value of 3)  in memory
# 3 is not constant but Object of INTEGER data type.

# print(a.real) : 3
# print(a.imag) : 0

b = 3;
# print(a is b) : True
# It means a and b point at same thing.

import sys

# print(sys.getrefcount(5)) : 28

c = 5
# print(sys.getrefcount(5)) : 30
# print(sys.getrefcount(c)) : 29


### How to make Variables ###

a, b = ('python', 'life') # using tuple
# print(a) : 'python'
# print(b) : 'life'
	
[a, b] = ['python', 'life'] # using list
# print(a) : 'python'
# print(b) : 'life'

a = b = 'Python'
# print(a) : 'Python'
# print(b) : 'Python'

a = 3
b = 5
a, b = b, a # swap
# a : 5
# b : 3


### Delete a varibale in memory ###

del(a)
del(b)


###  Copy a variable ###

a = [1, 2, 3]
a = [1, 2, 3]
b = a # not copy
a[1] = 4
# print(a) : [1, 4, 3]
# print(b) : [1, 4, 3]

a = [1, 2, 3]
b = a[:]
a[1] = 5
# print(a) : [1, 5, 3]
# print(b) : [1, 2, 3]

from copy import copy
# using copy module

a = [1, 2, 3]
b = copy(a)
a[1] = 5
# print(a) : [1, 5, 3]
# print(b) : [1, 2, 3]

print(b is a) # False



