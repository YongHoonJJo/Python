### About Boolean ###

# "python" 	: True
# "" 		: F
# [1,2,3]	: True
# []		: F
# ()		: F
# {}		: F
# 1			: True
# 0			: F
# None		: F

a = [1, 2, 3, 4]
while a:
	print(a.pop())

# 4
# 3 
# 2
# 1

if []:
	print('True')
else: # Caution!! ':'
	print("False")

# 'False'
