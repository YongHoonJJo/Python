### How to make String ###

"Hello World"
'Python is fun'
"""Life is too short, You need python"""
''' Life is too short, You need python'''

food = "Python's favorite food is perl"
# 'Python's favorite food is perl' (x)
say = '"Python is very easy." he says.'

food = 'Python\'s favorite food is perl!'
say = "\"Python is very easy.\" he says.."

multiLine = "Life is too short\nYou need python"

multiLine="""
Life is too short
You need python!
"""

multiLine='''
Life is too short
You need python!!
'''


### String Operation ###

head = "Python"
tail = " is fun!"
# print(head+tail)

a = "Python"
# print(a*2)

# print("="*20)
# print("My Program")
# print("="*20)


### String Indexing ###

a = "Life is to sort, You need Python"
# a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', ...
# a[-1]:'n', a[-2]:'o', ...
# a[0:4] : 'Life'
# a[0:3] : 'Lif'
# a[19:] : 'You need Python'
# a[:17] : 'Life is too short'
# a[:] : 'Life is to sort, You need Python'
# a[19:-7] : 'You need'

b = "20010331Rainy"
# b[:8] : '20010331'
# b[8:] : 'Rainy'
# b[:4] : '2001'
# b[4:8] : '0331'


### How to change String Element ###

c = "Pithon"
# c[1] = 'y' (x)
c = c[:1] + 'y' + c[2:]


### String Formating

d = "I eat %d apples." % 3
e = "I eat %s apples." % "five"

num = 7
f = "I eat %d apples." % num

day = "three"
g = "I ate %d apples. so I was sick for %s days." % (num, day)

# about %s ... not only String but also anything (parsing)
h = "I have %s apples" % 3
i = "PI is %s" % 3.141592

j = "Error is %d%%." % 98

# align and whitespace
k = "%-10sJane." % "hi" # Left align
l = "%10s" % "hi"		# Right align

# floating point
m = "%0.4f" % 3.141592  # 3.1416
n = "%10.4f" % 3.141592 #     3.1416


### String Methods ###

o = "hobby"
o.count('b') # 2

p = "Python is best choice"
p.find('i') # 7
p.find('k') # -1

q = "Life is too short"
q.index('t') # 8
# q.index('k') is error

r = ","
s = r.join('abcd') # a,b,c,d

t = "hi"
T = t.upper() # HI

u = "HI"
U = u.lower()

v = " hi "
w = v.lstrip() # 'hi '
x = v.rstrip() # ' hi'
y = v.strip() # 'hi'

z = "Life is too sort"
Z = z.replace("Life", "Your leg")

L = z.split() # ['Life', 'is', 'too', 'sort']
# z.split(':') == ['Life is too sort']

aa = "A:B:C:D"
LL = aa.split(':') # ['A', 'B', 'C', 'D']


### Advanced String Formating ###

bb = "I eat {0} apples".format(3)
cc = "I eat {0} apples.".format("five")

num = 5
dd = "I eat {0} apples.".format(num)

day = "three"
ee = "I ate {0} apples. so I was sick for {1} days.".format(num, day)
ff = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

gg = "{0:<10}".format("hi") # 'hi        '
hh = "{0:>10}".format("hi") # '        hi'
ii = "{0:^10}".format("hi") # '    hi    '

jj = "{0:=^10}".format("hi") # '====hi===='
kk = "{0:!<10}".format("hi") # 'hi!!!!!!!!'

PI = 3.141592
ll = "{0:0.4f}".format(PI) # 3.1416

mm = "{{ and }}".format() # '{ and }'

