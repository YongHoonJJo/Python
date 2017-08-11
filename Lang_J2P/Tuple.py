### How to make Tuple ###

t1 = ()
t2 = (1, ) # only one element
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# It is impossible to delete or to replace elements.

t = (1, 2, 'a', 'b')
# del t[0] (error)
# t[0] = 'c' (error)


### Indexing, Slicing, Operator ###

t = (1, 2, 'a', 'b')
# t[0] : 1
# t[3] : 'b'

# t[1:] : (2, 'a', 'b')

tt = (3, 4)
ttt = t + tt
#print(ttt) : (1, 2, 'a', 'b', 3, 4)

tt = tt * 3
#print(tt) : (3, 4, 3, 4, 3, 4)


### The others are similar to List. ###
