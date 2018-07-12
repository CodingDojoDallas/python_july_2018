def randint(n):
	import random
	first = n/5
	second = n/10
	print(int(random.random()*first))
	print(int(random.random()*second))
	print(int(random.random(1,2)*second))
	print(int(random.random(.01,1)*n))
randint(500)