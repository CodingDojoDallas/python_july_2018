import unittest
# 1. reverseList - Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.

# def reverseList(list):
#     for i in range(int(len(list)/2)):
#         list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
#     return list
#     pass
#
# class reverseListTests(unittest.TestCase):
#     def testTwo(self):
#         self.assertTrue(reverseList([1, 2, 3],), ([3, 2, 1]))
#
#     def testThree(self):
#         self.assertEqual(reverseList([4, 5, 6]), ([6, 5, 4]), True)
#
#     def testFour(self):
#         self.assertEqual(reverseList([7, 8, 9, 10]), ([10, 9, 8, 7]), True)
#
#     def setUp(self):
#         print("running setUp")
#
#     def tearDown(self):
#         print("running tearDown tasks")
#
# if __name__ == '__main__':
#     unittest.main()

# 2. isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').
#
def isPalindrome(str):
    for i in range(int(len(str)/2)):
        if str[i] == str[len(str)-1-i]:
            continue

        else:
            return False

    return True
#
# class isPalindromeTests(unittest.TestCase):
#     def testOne(self):
#         self.assertTrue(isPalindrome("anna"))
#
#     def testTwo(self):
#         self.assertTrue(isPalindrome("civic"))
#
#     def testThree(self):
#         self.assertEqual(isPalindrome("twenty"), False)
#
#     def testFour(self):
#         self.assertEqual(isPalindrome("trip"), False)
#
#     def testFive(self):
#         self.assertEqual(isPalindrome("grow up scrub"), False)
#
#     def setUp(self):
#         print("running setUp")
#
#     def tearDown(self):
#         print("running tearDown tasks")
#
# if __name__ == '__main__':
#     unittest.main()

# 3. coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().

# def coins(cents):
#     coinList = []
#     quarters = 0
#     dimes = 0
#     nickels = 0
#     pennies = 0
#     while cents != 0:
#         if cents >= 25:
#             cents -= 25
#             quarters += 1
#
#         elif cents >= 10:
#             cents -= 10
#             dimes += 1
#
#         elif cents >= 5:
#             cents -= 5
#             nickels += 1
#
#         elif cents >= 1:
#             cents -= 1
#             pennies += 1
#
#     coinList.append(quarters)
#     coinList.append(dimes)
#     coinList.append(nickels)
#     coinList.append(pennies)
#     return coinList
#
# class coinsTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(coins(87), ([3, 1, 0, 2]))
#
#     def testTwo(self):
#         self.assertEqual(coins(92), ([3, 1, 1, 2]))
#
#     def testThree(self):
#         self.assertNotEqual(coins(20), ([1, 1, 1, 1]))
#
#     def testFour(self):
#         self.assertNotEqual(coins(65), ([2, 1, 1, 1]))
#
#     def testFive(self):
#         self.assertNotEqual(coins(100), ([3, 2, 1, 0]))
#
#     def setUp(self):
#         print("Running setUp")
#
#     def tearDown(self):
#         print("Running tearDown")
#
# if __name__ == '__main__':
#     unittest.main()

# 4. Factorial (hacker challenge). Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).

# def Factorial(int):
#     product = 1
#     if int == 1:
#         return 1
#
#     product = int * Factorial(int - 1)
#     # for i in range(int, 1, -1):
#     #     product = product * i
#     return product
#
# class FactorialTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(Factorial(5), (120))
#
#     def testTwo(self):
#         self.assertEqual(Factorial(4), (24))
#
#     def testThree(self):
#         self.assertEqual(Factorial(3), (6))
#
#     def testFour(self):
#         self.assertNotEqual(Factorial(2), (1))
#
#     def testFive(self):
#         self.assertNotEqual(Factorial(6), (700))
#
#     def setUp(self):
#         print("Running setUp")
#
#     def tearDown(self):
#         print("Running tearDown tasks")
#
# if __name__ == '__main__':
#     unittest.main()

# 5. Fib (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).

# def fib(int):
#     sum = 0
#     if int == 0:
#         return 0
#
#     if int == 1:
#         return 1
#
#     sum = fib(int-2) + fib(int-1)
#     return sum
#
# class fibTests(unittest.TestCase):
#     def testOne(self):
#         self.assertEqual(fib(3), (2))
#
#     def testTwo(self):
#         self.assertEqual(fib(4), (3))
#
#     def testThree(self):
#         self.assertEqual(fib(5), (5))
#
#     def testFour(self):
#         self.assertNotEqual(fib(6), (2))
#
#     def testFive(self):
#         self.assertNotEqual(fib(7), (4))
#
#     def setUp(self):
#         print("Running setUp")
#
#     def tearDown(self):
#         print("Running tearDown tasks")
#
# if __name__ == '__main__':
#     unittest.main()
