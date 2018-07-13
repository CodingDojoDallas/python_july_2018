# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

# def countdown(num):
#     newarr=[]
#     for i in range(num,-1,-1):
#         newarr.append(i)
#     return newarr
# print(countdown(10))

# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

# def printandreturn(arr):
#     print(arr[0])
#     return arr[1]
# print(printandreturn([5,6]))

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

# def firstpluslength(arr):
#     sum=arr[0]+len(arr)
#     return sum
# print(firstpluslength([1,2,3,4,5]))

# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False

# def greaterthansecond(arr):
#     if len(arr)==1:
#         return False
#     newarr=[]
#     count=0
#     for i in range(0,len(arr)):
#         if arr[i]>arr[1]:
#             newarr.append(arr[i])
#             count=count+1
#     print(count)
#     return newarr
# print(greaterthansecond([1,3,4,5,2,2,3,4,5]))

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].

# def lengthAndValue(size,value):
#     newarr=[]
#     for i in range(0,size):
#         newarr.append(value)
#     return newarr
# print(lengthAndValue(4,7))

