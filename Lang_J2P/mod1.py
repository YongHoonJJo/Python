def sum(a, b):
	return a + b;

def safe_sum(a, b):
	if type(a) != type(b):
		print("You can't add a to b")
		return 
	else:
		return sum(a, b)

if __name__ == "__main__": 
	print(safe_sum('a', 1))
	print(safe_sum(1, 4))
	print(sum(10, 10.4))

# When this file execute directly (python3 mod1.py), 
# __name__ == "__main__" is true

# otherwise (in interpreter or import this file) is false.


