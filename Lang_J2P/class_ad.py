### class more ###

class Cal:
	pass

a = Cal()
print(type(a)) # <class '__main__.FourCal'>

class FourCal:
	def setData(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		result = self.first + self.second
		return result

a = FourCal()
a.setData(4, 2)
print(a.first) # 4
print(a.second) # 2

b = FourCal()
b.setData(3, 7)
print(b.first) # 3
print(b.second) # 7

print(a.sum()) # 6
print(b.sum()) # 10


### Class Park ###

class HousePark:
	lastName = "Park"

	def setName(self, name):
		self.fullName = self.lastName + name

pey = HousePark()
pes = HousePark()

print(pey.lastName) # "Park"
print(pes.lastName) # "Park"

pey.setName("CH")
print(pey.fullName) # "ParkCH"


class HouseParkInit:
	lastName = "Park"

	def __init__(self, name):
		self.fullName = self.lastName + name
	def travel(self, where):
		print("%s wanna to go on a trip to %s." % (self.fullName, where))

pey = HouseParkInit("BK")
pey.travel("Japan") # ParkBK wanna to go on a trip to Japan.


### Inheritance ###

class HouseKim(HouseParkInit):
	lastName = "Kim"

J = HouseKim("SR")
J.travel("China") # KimSR wanna to go on a trip to China.


### Method overriding ###

class HouseJo(HouseParkInit):
	lastName = "Jo"
	def travel(self, where):
		print("%s want to go on a trip to %s..!!" % (self.fullName, where))

J = HouseJo("YH")
J.travel("America") # "JoYH want to go on a trip to America..!!"


### Operator Overloading ###

class HouseBaek:
	lastName = "Baek"
	def __init__(self, name):
		self.fullName = self.lastName + name


class HouseSong:
	lastName = "Song"
	def __init__(self, name):
		self.fullName = self.lastName + name
	def travel(self, where):
	 	print("%s went on a trip to %s." % (self.fullName, where))
	def __add__(self, other):
		print("%s is going out with %s...S2" % (self.fullName, other.fullName))

SH = HouseBaek("SH")
JE = HouseSong("JE")

JE + SH # "SongJE is going out with BaekSH...S2"

# - : __sub__
# * : __mul__
# / : __truediv__


