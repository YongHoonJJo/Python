# Day_01_04_Function.py

# 함수의 핵심 : 데이터를 넘겨주고 넘겨받기
# 매개변수 : 넘겨주는 데이터
# 리턴값 : 넘겨받는 데이터


# 매개변수 없고, 반환값도 없고.
def f1():
    print('f1')


f1()    # f1


# 매개변수 있고, 반환 값 없고
def f2(a, b):
    print('f2', a, b)


f2(23, 'abc')   # f2 23 abc


# 매개변수 없고, 반환 값 있고.
def f3():
    # pass      # 아직 코딩 전이라는 뜻..
    print('f3')
    return 17


a = f3()
print(a)        # 17
print(f3())     # 17


# 매개변수 있고, 반환 값 있고.
# 두 자리 양수를 거꾸로 뒤집는 함수 만들기
def f4(num):
    return num%10*10 + num//10


print(f4(25))    # 52


# 문제
# 두 개의 정수 중에서 큰 숫자를 찾는 함수
def max2(a, b):
    if(a > b):
        return a
    return b


print(max2(3, 7))   # 7
print(max2(7, 3))   # 7


# 문제
# 네 개의 정수 중에서 큰 숫자를 찾는 함수
def max4(a, b, c, d):
    x, y = max2(a, b), max2(c, d)
    return max2(x, y)


print(max4(3, 9, 1, 7))