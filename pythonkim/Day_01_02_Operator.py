# Day_01_02_Operator.py


# 연산자 : 산술, 관계, 논리, 비트

# 산술 : +    -    *    /    //   %   **
a, b = 17, 5
print(a+b)      # 22
print(a-b)      # 12
print(a*b)      # 85
print(a/b)      # 3.4
print(a//b)     # 3
print(a%b)      # 2 , mod
print(a**b)     # 1419857, 17^5

# 문제
# 두 자리 양수를 거꾸로 뒤집어 보기
# 37 -> 73

n = 37
a1 = n//10
a2 = n%10

n = a2*10 + a1
print(n)    # 73


# 관계 : > >= < <= == !=

a, b = 17, 5
print(a, b)

print(a > b)    # T
print(a >= b)   # T
print(a < b)    # F
print(a <= b)   # F
print(a == b)   # F
print(a != b)   # T


# 형변환(casting) : int, float, str, bool

print(int(True))    # 1
print('345')        # 345
print(int('345'))   # 345
print(int(a != b))  # 1
print(int(False))   # 0


# 문제
# 10대인지 판단해보기.

age = 15
b1 = age >= 10      # T, F
b2 = age <= 19      # T, F

# T * T = T
# T * F = F
# F * T = F
# F * F = F

print(bool(b1*b2))  # True
print(age >= 10  *  age <= 19)    # False
print((age >= 10) * (age <= 19))    # 1
print(10 <= age <= 19)      # True (python only)


# 논리 : and  or  not

print(True and True)    # True
print(True and False)    # False
print(False and True)    # False
print(False and False)    # False

print(age >= 10  and  age <= 19)    # True

