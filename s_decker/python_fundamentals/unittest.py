import unittest





# reverseList - Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.

# def reverseArray(list):
# 	for i in range(int(len(list)/2)):
# 		list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
# 	return list

# class reverseArrayTests(unittest.TestCase):
# 	def testOne(self):
# 		self.assertEqual(reverseArray([1,2,3]), [3,2,1])
# 	def testTwo(self):
# 		self.assertEqual(reverseArray([5,1,2,3]),[3,2,1,5])
# 	def setUp(self):
# 		print("running setUp")
# 	def tearDown(self):
# 		print("running tearDown tasks")

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').

# def isPal(string):
# 	for i in range(int(len(string)/2)):
# 		if string[i] == string[len(string)-i-1]:
# 			return True
# 		else:
# 			return False 
# class palTest(unittest.TestCase):
# 	def testOne(self):
# 		self.assertTrue(isPal("ana"))	
# 	def testTwo(self):
# 		self.assertTrue(isPal("geoge"))
# 	def testThree(self):
# 		self.assertTrue(isPal("racecar"))

# 	def setUp(self):
# 		print("running setUp")
# 	def tearDown(self):
# 		print("running tearDown tasks")


# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().

# def needChange(num):
# 	q=0
# 	d=0
# 	n=0
# 	p=0
# 	while num > 0:
# 		if num > 25:
# 			num = num - 25
# 			q = q + 1
			
# 		if num < 25 and num > 10:
# 			num = num - 10
# 			d = d + 1 
				
# 		if num < 10 and num > 5:
# 			num = num - 5
# 			n = n + 1
			
# 		if num < 5:
# 			num = num -1
# 			p = p + 1
			
# 	return num, q, d, n, p

# class coinTest(unittest.TestCase):
# 	def testOne(self):
# 		self.assertEqual(needChange(87), (0,3,1,0,2))
# 	def testTwo(self):
# 		self.assertEqual(needChange(73), (0,2,2,0,3))
# 	def testThree(self):
# 		self.assertEqual(needChange(42), (0,1,1,1,2))
# 	def testFour(self):
# 		self.assertEqual(needChange(17), (0,0,1,1,2))
# 	def testFive(self):
# 		self.assertEqual(needChange(4), (0,0,0,0,4))
# 	def setUp(self):
# 		print("running setUp")
# 	def tearDown(self):
# 		print("running tearDown")

# Factorial (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).

# def fact(num):
# 	if num > 1:
# 		num = num * fact(num-1)
# 	return (num)


# class factTest(unittest.TestCase):
# 	def testOne(self):
# 		self.assertEqual(fact(5), 120)



# Fib (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).

# def fib(num):
# 	if num == 0:
# 		return 0
# 	if num == 1:
# 		return 1
# 	if num > 1:
# 		num = fib(num-1)+fib(num-2)
# 	return num


# class fibTest(unittest.TestCase):
# 	def testOne(self):
# 		self.assertEqual(fib(10), (55))

if __name__ == '__main__':
	unittest.main()