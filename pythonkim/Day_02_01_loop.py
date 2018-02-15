# Day_02_01_loop.py

# 문제
# count 에 0~3 사이의 숫자를 입력 받아서
# 입력받은 숫자 만큼 아침인사를 해봅니다.
# 2가지 종류의 코드를 만들어보기.


def ans1():
    count = int(input('count : '))

    if count == 1:
        print("Good Morning!")
    elif count == 2:
        print("Good Morning!")
        print("Good Morning!")
    elif count == 3:
        print("Good Morning!")
        print("Good Morning!")
        print("Good Morning!")


def ans2():
    count = 2
    if count >= 1:
        print("Good Morning!")
    if count >= 2:
        print("Good Morning!")
    if count >= 3:
        print("Good Morning!")


def ans3():
    count = 2
    i = 0
    if i < count:
        print("Good Morning!")
        i += 1
        if i < count:
            print("Good Morning!")
            i += 1
            if i < count:
                print("Good Morning!")
                i += 1
                if i < count:
                    print("Good Morning!")
                    i += 1
                    if i < count:
                        print("Good Morning!")
                        i += 1


def ans():
    count = 3
    i = 0
    while i < count:
        print("Good Morning!")
        i += 1


# 규칙을 찾는 것이 중요. (시작, 종료, 증감)
# 1 3 5 7 9     1~9 까지 2칸씩 건너뛴다.
# 0 1 2 3 4     0~4 까지 1칸씩 건너뛴다.
# 5 4 3 2 1     5~1 까지 -1칸씩 건너뛴다.

def rule1():
    i = 1                   # 시작
    while i <= 9:           # 종료
        print("Hello")
        i += 2              # 증감


def rule2():
    i = 0
    while i <= 4:
        print("Hello")
        i += 1


def rule3():
    i = 5
    while i >= 1:
        print("Hello")
        i -= 1



print('Hello', end=' ')
print('python')

# 실행결과
# Hello python

print('Hello', end='***')
print('python')

# 실행결과
# Hello***python


# 문제
# 0~99 까지 출력하는 함수 만들기

def show100():
    i = 0
    while i <= 99:
        print(i, end=' ')
        i += 1


for i in range(0, 10, 1):
    print(i, end=' ')
print()

for i in range(0, 10):
    print(i, end=' ')
print()

for i in range(10):
    print(i, end=' ')
print()


# 문제
# for 문을 사용해서 100보다 작은 양의 홀수와 짝수 합계를
# 각각 구하는 함수를 작성
# 함수 리턴값은 여러 개 가능

def sumOfOddEven():
    odd, even = 0, 0
    for i in range(1, 100):
        if i%2 == 1: odd  += i
        else :       even += i

    return odd, even


s1, s2 = sumOfOddEven()
print(s1, s2)       # 2500 2450

print('-'*50)

import random

print(random.randrange(10))
print(random.randrange(10, 20))
print(random.randrange(10, 20, 2))


# Placeholder

for _ in range(5):
    print(random.randrange(10), end=' ')
print()


random.seed(1)
for _ in range(5):
    print(random.randrange(10), end=' ')    # 2 9 1 4 1
print()

next = 1
def rand():
    global next
    next = next * 1103515245 + 12345
    return int(next // 65536) % 32768




