### while ###

threeHit = 0
while threeHit < 10:
	threeHit += 1
	print("count %d" % threeHit)
	if threeHit == 10:
		print("End of While")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

num = 4
while num != 4:
	print(prompt)
	num = int(input())
	print("Your input: %d" % num)

coffee = 1 
money = 400
while money:
	print('get coffee')
	coffee -= 1
	money -= 300
	print('rest: %d' % coffee)
	if not coffee:
		print('sold out')
		break

coffee = 1 
while True:
	money = int(input("insert coin: "))
	if money == 300:
		print('get coffee')
		coffee = coffee - 1
	elif money > 300:
		print('get coffee and change: %d' % (money-300))
		coffee = coffee - 1
	else:
		print('Not enough money')
	if not coffee:
		print('sold out')
		break

a = 0
while a < 10:
	a = a+1
	if a % 2 == 0 : continue
	print(a)
else:
	print("End of while")


