### Class ###

class Calculator:
	def __init__(self):
		self.result = 0

	def adder(self, num):
		self.result += num
		return self.result

	def sub(self, num):
		self.result -= num
		return self.result
	
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3)) # 3
print(cal1.adder(4)) # 7
print(cal2.adder(3)) # 3
print(cal2.adder(7)) # 10


### Class variable ###

class Service:
	secret = "You are a ..."

pey = Service()
print(pey.secret)# "You are a ..."

# secret is class variable !!
print(Service.secret) # "You are a ..."

Service.secret = "You are our hero!"
print(pey.secret) # "You are our hero!"


### Method ###

class ServiceM:
	secret = "You are a ...."
	def sum(self, a, b):
		result = a + b
		print("%s + %s = %s..!!" % (a, b, result))

s = ServiceM()
s.sum(1, 1) # 1 + 1 = 2..!!


### about self ###

# Both have same result!
s.sum(2, 3) # 2 + 3 = 5..!!
ServiceM.sum(s, 2, 3) # 2 + 3 = 5..!!


### Object(Member) variable ###

class ServiceObj:
	secret = "Object variable"
	def setName(self, name):
		self.name = name;
	def sum(self, a, b):
		result = a + b
		print("Hey %s, %s + %s = %s." % (self.name, a, b, result));

J = ServiceObj()
J.setName("Hoon") 
J.sum(1, 2) # "Hey Hoon, 1 + 2 = 3."

J.name = "YH"
J.sum(1, 2) # Hey YH, 1 + 2 = 3.


### __init__ ###

babo = ServiceObj()
# babo.sum(1,1) : error..!!

class ServiceInit:
	secret = "__init__"
	def __init__(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("Hey %s, %s + %s = %s." % (self.name, a, b, result));

i = ServiceInit("Hoooon")
i.sum(3, 4) # Hey Hoooon, 3 + 4 = 7.




