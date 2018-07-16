class MathDojo:

	def __init__(self):
		self.total = 0

	def add(self,*num):
		for i in range(len(num)):
			if type(num[i]) is tuple:
				for j in num[i]:
					self.total += j
	return self

	def sub(self,*num):
		for i in range(len(num)):
			if type(num[i]) is tuple:
				for j in num[i]:
					self.total -= j
	return self

	def result(self):
		print (self.total)

md = MathDojo().add(1,5,8).sub(4).result()