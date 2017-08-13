number = 23
running = True

while running :
	guess = int(raw_input('Enter the integer: '))
	
	if guess == 23:
		print 'OK'
		running = False
	elif guess < 23:
		print 'UP'
	else :
		print 'DOWN'
else:
	print 'while done'


