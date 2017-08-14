def total(initial=5, *numbers, **keywords):
	print keywords
	count = initial
	for num in numbers:
		count += num
	for key in keywords:
		count += keywords[key]
	return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)
# 166

# initail = 10
# numbers = (1, 2, 3)
# keywords = {'vegetables': 50, 'fruits': 100}
