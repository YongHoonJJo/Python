### for variable in list(tuple, string)  ###

L = ['one', 'two', 'three']
for i in L:
	print(i)

# tuple in list	
a = [(1,2), (3,4), (5,6)]
for (s, e) in a:
	print(s + e)

# range(10 make a object of range that includes from 0 to 9
a = range(10)
print(a)

Sum = 0;
for i in range(1, 11):
	Sum += i;
print(Sum)

mark = [90, 25, 67, 45, 80]
for idx in range(len(mark)):
	if mark[idx] < 60: continue
	print("No.%d is passed" % (idx+1))

for dan in range(2,10):
	for i in range(1,10):
		print(dan*i, end=" ") # print i*j, for python2.7
	print('')

# 2 4 6 8 10 12 14 16 18 
# 3 6 9 12 15 18 21 24 27 
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54 
# 7 14 21 28 35 42 49 56 63 
# 8 16 24 32 40 48 56 64 72 
# 9 18 27 36 45 54 63 72 81


### including for statement in list ###
	
a = [1, 2, 3, 4]
res = []
for num in a:
	res.append(num*3)

result = [num * 3 for num in a]
print(res) # print(result)

result = [num * 3 for num in a if num%2==0]
print(result)

nine = [x*y for x in range(2, 10)
			for y in range(1, 10)]
print(nine)


