# Day_02_02_list.py


a = [1, 3, 5]
print(a)    # [1, 3, 5]
print(a[0], a[1], a[2])     # 1 3 5

a[0] = 99
print(a)    # [99, 3, 5]


for i in range(len(a)):
    print(a[i])


# 문제
# 100 보다 작은 난수 10개로 이루어진 리스트를  반환하는 함수 만들기


import random


def makeRandom():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(10):
        a[i] = random.range(100)
    return a


def makeRandom2():
    a = [0]*10
    for i in range(10):
        a[i] = random.range(100)
    return a


def makeRandom3():
    a = []
    for i in range(10):
        a.append(random.randrange(100))
    return a


random.seed(19)
a = makeRandom3()
print(a)


# 문제
# 리스트를 거꾸로 뒤집는 함수를 만드시오.


def reverseList(c):
    size = len(c)
    for i in range(size//2):
       c[i], c[size-1-i] = c[size-1-i], c[i]
    return c


print(reverseList(a))


for i in a:
    print(i, end=' ')
print()


print(type(range(5)), type(a))  # <class 'range'> <class 'list'>


for i in a:
    print(i, end=' ')
print()
# 37 67 44 50 25 65 15 66 5 86

for i in reversed(a):
    print(i, end=' ')
print()
# 86 5 66 15 65 25 50 44 67 37

for i in reversed(range(len(a))):
    print(a[i], end=' ')
print()
# 86 5 66 15 65 25 50 44 67 37

for i in enumerate(a):
    print(i, end=' ')
print()
# (0, 37) (1, 67) (2, 44) (3, 50) (4, 25) (5, 65) (6, 15) (7, 66) (8, 5) (9, 86)

for i in enumerate(a):
    print(i[0], i[1], end=' ')
print()
# 0 37 1 67 2 44 3 50 4 25 5 65 6 15 7 66 8 5 9 86

t = (1, 2, 3)
# t[0] = 99
# TypeError: 'tuple' object does not support item assignment


def sumOfOddEven():
    odd, even = 0, 0
    for i in range(1, 100):
        if i%2 == 1: odd  += i
        else :       even += i

    return odd, even


s1, s2 = sumOfOddEven()
print(s1, s2)       # 2500 2450

s = sumOfOddEven()
print(s)            # (2500, 2450)
print(type(s))      # <class 'tuple'>

t = 1, 2
print(t)            # (1, 2)
print(type(t))      # <class 'tuple'>


for i, k in enumerate(a):
    print(i, k, end=' ')
print()

print('-'*50)

a = list(range(0, 10, 2))
print(a)    # [0, 2, 4, 6, 8]

b = a;
a[0] = 99
print(a)    # [99, 2, 4, 6, 8]
print(b)    # [99, 2, 4, 6, 8]


a = list(range(0, 10, 2))
print(a)    # [0, 2, 4, 6, 8]

b = a.copy();
a[0] = 99
print(a)    # [99, 2, 4, 6, 8]
print(b)    # [0, 2, 4, 6, 8]


a = list(range(0, 10, 2))
print(a)    # [0, 2, 4, 6, 8]
print(a[0], a[-1])      # 0 8