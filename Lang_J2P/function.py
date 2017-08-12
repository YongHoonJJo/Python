### Function ###

def Sum(a, b):
	ret = a + b
	return ret

res = Sum(1, 2)
print(res)


def say():
	return 'Hi'

a = say()
print(a)

def sayHello():
	print("Hello")

a = sayHello()
print(a) # None


### lots of parameters ###

# args in *args means tuple.
def sum_many(*args):
	ans = 0
	for i in args:
		ans += i
	return ans

res = sum_many(1, 2, 3)
print(res)

res = sum_many(1, 2, 3, 4, 5)
print(res)

def sum_mul(choice, *args):
	if choice == 'sum':
		ret = 0
		for i in args:
			ret += i
	elif choice == "mul":
		ret = 1
		for i in args:
			ret *= i
	return ret

res = sum_mul('sum', 1, 2, 3, 4, 5)
print(res) # 15

res = sum_mul('mul', 1, 2, 3, 4, 5)
print(res) # 120

# dic in **dic means dictionary.

def total(init=5, *numbers, **keywords):
	cnt = init
	for n in numbers:
		cnt += n
	for key in keywords:
		cnt += keywords[key]
	return cnt

# vegetables=50 : dictionary
# 1, 2, 3 : tuple
ret = total(10, 1, 2, 3, vegetables=50, fruits=100)
print("total(10, 1, 2, 3, vegetables=50, fruits=100)")
print(ret)

### Function returns Only one value ###

def sum_and_mul(a, b):
	return a+b, a*b # return tuple

res = sum_and_mul(3, 4)
print(res) # (7, 12)

s, m = sum_and_mul(3, 4)
print(s) # 7
print(m) # 12

def say_nick(nick):
	if nick == "babo":
		return
	print("nick is %s." % nick)

say_nick("babo")


### Initializing parameters ###

def say_myself(name, old, man=True):
	print("My name is %s." % name)
	print("I'm %d years old." % old)
	if man: print("Man!")
	else: print("Woman!")

say_myself("Tom", 27)
say_myself("Jane", 27, False)


### Scope ###

a = 1
def varTest(a):
	a = a + 1 # a in varTest is local.

varTest(a)
print(a) # 1

def varGlobal():
	global a
	a = a+100

varGlobal()
print(a) # 101

