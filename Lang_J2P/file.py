### File I/O ###

# mode r : read
# mode w : write
# mode a : append
f = open("./text.txt", 'w')
for i in range(1, 11):
	data = "Line %d\n" % i
	f.write(data)
f.close()

f = open("./text.txt", 'r')
line = f.readline()
print(line) # "Line 1\n"
line = f.readline()
print(line) # "Line 2\n"
f.close()

f = open("./text.txt", 'r')
while True:
	line = f.readline()
	if not line: break # if reach EOF, return None
	print(line)
f.close()

# readlines() Method
f = open("./text.txt", 'r')
lines = f.readlines() # ..s
# lines is ["Line 1\n","Line 2\n",..., "Line 10.\n"] : List
for line in lines:
	print(line)
f.close()

# read() Method
f = open("./text.txt", 'r')
data = f.read()
# data is "Line 1.\nLine 2.\n ... Line 10.\n" : string
print(data)
f.close()


### append mode ###

f = open("./text.txt", 'a')
for i in range(11, 20):
	data = "Line %d.\n" % i
	f.write(data)
f.close()


### with ###

# U don't need to declare f.close()
with open("./foo.txt", 'w') as f:
	f.write("Life is too short, you need python")

### using sys module ###

import sys

args = sys.argv[1:]
for i in args:
	print(i)

# python3 file.py hi
# args[0] is file.py
# args[1] is hi


