### How to make Set ###

s1 = set([1, 2, 3])
# print(s1) : {1, 2, 3}

s2 = set("Hello")
# print(s2) : {'l', 'e', 'H', 'o'}

# Don't allow redundancy.
# Unordered so that don't support indexing.

l1 = list(s1)
# print(l1) : [1, 2, 3]

t1 = tuple(s1)
# print(t1) : (1, 2, 3)


### Usage ###

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

intersection = s1 & s2
# print(intersection) : {4, 5, 6}

s3 = s1.intersection(s2)
# print(s3) : {4, 5, 6}

union = s1 | s2
# print(union) : {1, 2, 3, 4, 5, 6, 7, 8, 9}

s4 = s1.union(s2)
# print(s4) : {1, 2, 3, 4, 5, 6, 7, 8, 9}

diff = s1 - s2
# print(diff) : {1, 2, 3}

diff = s2 - s1
# print(diff) : {8, 9, 7}

s5 = s1.difference(s2) # {1, 2, 3}
s6 = s2.difference(s1) # {8, 9, 7}


### Methods ###

s = set([1, 2, 3])
s.add(4)
# print(s) : {1, 2, 3, 4}

s.update([5, 6, 7])
# print(s) : {1, 2, 3, 4, 5, 6, 7}

s.remove(3)
# print(s) : {1, 2, 4, 5, 6, 7}

