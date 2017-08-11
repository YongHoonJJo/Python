### if ... else ... ###

money = 1

if money:
	print("by taxi")
else:
	print('by walk')
# 'by taxi'

money = 2000
if money >=3000:
	print("by taxi")
else:
	print('by walk')
# 'by walk'


### and, or, not ###

money = 2000
card = 1
if money >=3000 or card:
	print("by taxi")
else:
	print('by walk')
# 'by taxi'


### x in s, x not in s ###

# s includes list, tuple ans string.

if 1 in [1, 2, 3]:
	print('1 in list')

if 'a' not in ('b', 'c', 'd'):
	print("'a' not in tuple")

if 'j' not in 'python':
	print("'j' not in 'python'")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print('get card')

### elif ###

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
	print('by bus')
elif card:
	print('by taxi')
else:
	print('by walk')





