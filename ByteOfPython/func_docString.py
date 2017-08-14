def print_max(x, y):
	''' Prints the maximum of two numbers.

	The two values must be integers. '''

	# converto to integers, if possible
	x = int(x)
	y = int(y)

	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

print_max(3, 5)
# 5 is maximum

print print_max.__doc__
# Prints the maximum of two numbers.
#
#	 	The two values must be integers.

help(print_max)
#
#	Help on function print_max in module __main__:
#
#	print_max(x, y)
#	    Prints the maximum of two numbers.
#		    
#		    The two values must be integers.
#	(END)
