# Day_01_05_re.py

import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

print(db)

# 3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534


ns = re.findall(r'[0-9]', db) # 숫자
print(ns)

# ['3', '4', '1', '2', '1', '2', '3', '3', '8', '3', '4', '3', '3', '3', '1', '2', '4', '8', '6', '3', '4', '1', '4', '2', '3', '5', '6', '7', '2', '5', '6', '7', '4', '3', '5', '3', '5', '6', '7', '5', '3', '5', '1', '5', '4', '8', '5', '3', '4']


ns = re.findall(r'[0-9]+', db) # 숫자 한개 이상
print(ns)

# ['3412', '123', '3834', '333', '1248', '634', '1423', '567', '2567', '435', '3567', '535', '1548', '534']


# 문제
# 이름만 찾아보기
# names = re.findall(r'[a-zA-Z]+', db)
names = re.findall(r'[A-Z][a-z]+', db)  # 처음 대문자 한글자 + 소문자 한개 이상.
print(names)

# ['Bob', 'Jonny', 'Kate', 'Tony', 'Peter', 'Alice', 'Kerry']


# 문제
# T로 시작하는 이름
# T로 시작하지 않는 이름

Tname = re.findall(r'T[a-z]+', db)
print(Tname)    # ['Tony']

nTname = re.findall(r'[^T][a-z]+', db)  # bug
print(nTname)   # ['Bob', 'Jonny', 'Kate', 'ony', 'Peter', 'Alice', 'Kerry']

nTname = re.findall(r'[A-SU-Z][a-z]+', db)
print(nTname)   # ['Bob', 'Jonny', 'Kate', 'Peter', 'Alice', 'Kerry']
