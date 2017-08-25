### kind of Error ###

# f = open("없는파일", 'r')
# FileNotFoundError // IOError (2.7)

# 4 / 0
# ZeroDivisionError

# a = [1, 2, 3]
# print(a[4])
# IndexError


### Try, Except ###

# try:
#	...
# except [발생 오류[as 오류 메세지 변수]]:
#	...
# []는 생략가능

try:
	4 / 0
except ZeroDivisionError as e: 	# except ZeroDivisionError, e: (2.7)
	print(e) # "division by zero"

try:
	4 / 2
except ZeroDivisionError as e: 	# except ZeroDivisionError, e: (2.7)
	print(e) # "division by zero"
else:
	print("예외가 발생하지 않은 경우 실행됨")


try:
	4 / 0 
except ZeroDivisionError as e: 	# except ZeroDivisionError, e: (2.7)
	print(e) # "division by zero"
else:
	print("예외가 발생하지 않은 경우 실행됨")
finally:
	print("예외가 발생하든 안하든 실행됨")


try:
	4 / 2
except ZeroDivisionError as e: 	# except ZeroDivisionError, e: (2.7)
	print(e) # "division by zero"
else:
	print("예외가 발생하지 않은 경우 실행됨")
finally:
	print("예외가 발생하든 안하든 실행됨")


### Several excepts ###

try:
	a = [1, 2]
	print(a[3])
	4/0 # 위 라인에서 오류발생하므로 여기는 실행되지 x
except ZeroDivisionError:
	print("0으로 나눌 수 x")
except IndexError:
	print("indexing 불가능")

try:
	a = [1, 2]
	print(a[3])
	4 / 0 # 실행되지 x
except (ZeroDivisionError, IndexError) as e:
	print(e) # "list index out of range"


### avoiding Error ###

try:
	f = open("없는파일", 'r')
except FileNotFoundError:
	pass


### Trigger an Error intentionally  ###

# Python 내장 클래스인 Exception 클래스를 상속
class MyError(Exception):
	def __str__(self):
		return "허용되지 않은 별명"

def say_nick(nick):
	if nick == 'babo':
		raise MyError()
	print(nick)

say_nick('angel') # "angel"
#say_nick('babo')

# Traceback (most recent call last):
#   File "TryExcept.py", line 94, in <module>
#     say_nick('babo')
#   File "TryExcept.py", line 90, in say_nick
#     raise MyError()
# __main__.MyError: 허용되지 않은 별명

try:
	say_nick('angel') # "angel"
	say_nick('babo')
except MyError as e:
	print(e) # "허용되지 않은 별명"


# 오류메세지를 에러발생 시점마다 전달하기
class MyError2(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return self.msg

def say_hello(msg):
	if msg != 'hello':
		raise MyError2("그건 인사가 아니자나!!")
	print(msg)

say_hello('hello')
say_hello('bye')
# Traceback (most recent call last):
#	File "TryExcept.py", line 125, in <module>
#	  say_hello('bye')
#	File "TryExcept.py", line 121, in say_hello
#	  raise MyError2("그건 인사가 아니자나!!")
# __main__.MyError2: 그건 인사가 아니자나!!
	
