# Day_01_01_Basic.py

print('Hello python!')

# 문제
# Hello, python! 을 3회 출력하는 코드를 3가지 만들어 보시오.

print('Hello python!Hello python!Hello python!')

print('Hello python!'*3)

print('Hello python!')
print('Hello python!')
print('Hello python!' 'Hello python!' 'Hello python!')

print("Hello python!" "Hello python!" "Hello python!")
# Hello python!Hello python!Hello python!

print(3.14, 56, "string", True)
print(type(3.14), type(56), type("string"), type(True))

a = 3.14
print(3.14, a, type(a))

a = 56
print(a, type(a))


print('Hell\no python!')    # newline, 개행문자

print('"Hello"')    # "Hello"
print("'Hello'")    # 'Hello'
print('-'*50)       # --------------------------------------------------


a = 7
b = 19
print(a, b)     # 7, 19

# 문제
# 아래쪽 코드에서 거꾸로 출력하도록 코드 추가하기
# a와 b를 서로 교환한다.

# a = 19
# b = 7     # 위에서 값을 변경하면 이 코드는 의미가 없어진다.


# 콜라와 주스가 담긴 컵이 있다. 내용물을 바꾸고 싶다. 어떻게?
tmp = a		# 빈컵이 필요..!!
a = b
b = tmp

print(a, b)


a, b = b, a
print(a, b)

# a = 7
# b = 19
a, b = 7, 19