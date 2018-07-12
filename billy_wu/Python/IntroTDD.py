# reverseList - Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  
# In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.

# import unittest
# # from forLoopBasicII import reverseList

# def reverseList(arr):
#     temp=0
#     for i in range(0,int(len(arr)/2)):
#         temp=arr[i]
#         arr[i]=arr[len(arr)-1-i]
#         arr[len(arr)-1-i]=temp
#     return arr
# class ReverseListTest(unittest.TestCase):
#     def test1(self):
#         return self.assertEqual(reverseList([1,3,5]),[5,3,1])
#     def test2(self):
#         return self.assertEqual(reverseList([1]),[1])
#     def test3(self):
#         return self.assertNotEqual(reverseList([-1,0,1]),[1,9,-1])
# if __name__ == "__main__":
#     unittest.main()

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  
# For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  
# Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  
# Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  
# (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').

# import unittest

# def isPal(word):
#     i=0
#     for i in range(int(len(word)/2)):
#         if word[i]==word[len(word)-1-i]:
#             continue
#         else:
#             return False
#         # if i >= (len(word)-1-i):
#         #     return True
#     return True
# class IsPalindrome(unittest.TestCase):
#     def test1(self):
#         return self.assertFalse(isPal("cheese"))
#     def test2(self):
#         return self.assertFalse(isPal("bamboozle"))
#     def test3(self):
#         return self.assertEqual(isPal("mom"), True)
# if __name__ == "__main__":
    # unittest.main()

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  
# For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  
# If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  
# Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  
# Add at least 5 other test cases first, before you fill in the codes inside function coin().

# import unittest

# def gimmeChange(num):
#     Q = 0
#     D = 0
#     N = 0
#     P = 0
#     coinz = []
#     Q = int(num/25)
#     print(Q)
#     coinz.append(Q)
#     num = num - (Q*25)
#     D = int(num/10)
#     print(D)
#     coinz.append(D)
#     num = num - (D*10)
#     N = int(num/5)
#     print(N)
#     coinz.append(N)
#     num = num - (N*5)
#     P = num
#     print(P)
#     coinz.append(P)
#     print(coinz)
#     return coinz
# class ChangeTest(unittest.TestCase):
#     def test1(self):
#         return self.assertEqual(gimmeChange(89), [3,1,0,4])
#     def test2(self):
#         return self.assertNotEqual(gimmeChange(89), [2,1,2,4])
#     # def test3(self):
#     #     return self.assertIs(gimmeChange(89), [3,1,0,4])
#     def test4(self):
#         return self.assertIsNot(gimmeChange(89), [2,1,2,4])
# if __name__ == "__main__":
#     unittest.main()


# Factorial (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  
# Do this using recursion; remember that factorial(n) = n * factorial(n-1).

# import unittest

# def fac(num):
#     if num == 0:
#         return 1
#     factorial=num*(fac(num-1))
#     print(factorial)
#     return factorial
# class Factorial(unittest.TestCase):
#     def test1(self):
#         return self.assertEqual(fac(5),120)
#     def test2(self):
#         return self.assertNotEqual(fac(5),100)
# if __name__ == "__main__":
#     unittest.main()


# Fib (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  
# Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).

# import unittest

# def fib(num):
#     if num == 1:
#         return 1
#     if num == 0:
#         return 0
#     fibbonacci = fib(num-2) + fib(num-1)
#     print(fibbonacci)
#     return fibbonacci
# class FibFib(unittest.TestCase):
#     def test1(self):
#         return self.assertEqual(fib(7), 13)
#     def test2(self):
#         return self.assertNotEqual(fib(5), 3)
# if __name__ == "__main__":
#     unittest.main()
