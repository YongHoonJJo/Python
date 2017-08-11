### How to make List ###

odd = [1, 3, 5, 7, 9]

a = [] # a = list()
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]


### Indexing and Slicing ###

b = [1, 2, 3]
# b[0] + b[2] : 4
# b[-1] : 3

h = [1, 2, 3,['a', 'b', 'c']]
# h[0] : 1
# h[3] : ['a', 'b', 'c']
# h[-1] : ['a', 'b', 'c']
# h[-1][0] : 'a'

i = [1, 2, ['a', 'b', ['Life', 'is']]]
# i[2][2][0] : 'Life'

odd = [1, 3, 5, 7, 9]
# odd[0:2] : [1, 3]
# odd[:2] : [1, 3]
# odd[2:] : [5, 7, 9]

k = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# k[2:5] : [3, ['a', 'b', 'c'], 4]
# k[3][:2] : ['a', 'b'] 


### List Operator ###

m = [1, 2, 3]
n = [4, 5, 6]
o = m+n # [1, 2, 3, 4, 5, 6]
p = m*3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# m[2] + "hi" (error)
q = str(m[2]) + "hi" # '3hi'


### Modify, Replace, Delete ###

r = [1, 2, 3]
r[2] = 4;
# print(r) : [1, 2, 4]

r[1:2] = ['a', 'b', 'c']
# print(r) : [1, 'a', 'b', 'c', 4]

r[1:3] = []
# print(r) : [1, 'c', 4]

del r[1]
# print(r) : [1, 4]

r = [1, 2, 3, 4, 5]
del r[1:4]
# print(r) : [1, 5]


### List Methods ###

s = [1, 2, 3]
s.append(4)
# print(s) : [1, 2, 3, 4]

t = [1, 4, 3, 2]
t.sort()
# print(t) : [1, 2, 3, 4]

u = ['a', 'c', 'b']
u.sort()
# print(u) : ['a', 'b', 'c']

v = ['a', 'z', 'b', 'x']
v.reverse()
# print(v) : ['x', 'b', 'z', 'a']

w = [1, 2, 3]
# w.index(3) : 2
# w.index(1) : 0
# w.index(0) : error

w.insert(0, 4)
# print(w) : [4, 1, 2, 3]

w.insert(3, 5)
# print(w) : [4, 1, 2, 5, 3]

x = [1, 2, 3, 1, 2, 3]
x.remove(3)
# print(x) : [1, 2, 1, 2, 3]

z = [1, 2, 3]
aa = z.pop()
# print(aa) : 3
# print(z) : [1,2]

zz = [1, 2, 1, 3, 1]
cnt = zz.count(1)
# print(cnt) : 3

z = [1, 2, 3]
z.extend([4, 5])
# print(z) : [1, 2, 3, 4, 5]

ex = [6, 7]
z.extend(ex)
# print(z) : [1, 2, 3, 4, 5, 6, 7]











