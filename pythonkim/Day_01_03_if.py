# Day_01_03_if.py

a = 13
print(a % 2)        # 1

if a%2 == 1:
    print('홀수')     # 홀수
else:
    print('짝수')

if a%2:              # 1 은 True
    print('홀수')     # 홀수
else:
    print('짝수')

if a:
    print(a)          # 13


# 문제
# 0 ~ 999 사이의 값을 입력 받아
# 몇 자리 숫자인지 맞춰보기

a = input("number : ")    # 키보드로 부터 입력을 기다린다., input 안의 문자열은 프롬프트
print(type(a))            # <class 'str'>

a = int(input("number : "))
print(type(a))            # <class 'int'>

if a >= 100:
    print(3)
else:
    if a >= 10:
        print(2)
    else:
        print(1)

print(     'Hello')
print(

    'Hello'
)
print(          'Hello')

if a >= 100:
    print(3)
elif a >= 10:
    print(2)
else:
    print(1)
