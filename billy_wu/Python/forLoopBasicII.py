# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

# def biggiesize(arr):
#     for i in range(0, len(arr)):
#         if arr[i]>0:
#             arr[i]="big"
#     return arr
# print(biggiesize([-1,3,5,-5]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).

# def countpositives(arr):
#     count=0
#     for i in range(0,len(arr)):
#         if arr[i]>0:
#             count=count+1
#     arr[len(arr)-1]=count
#     return arr
# print(countpositives([-1,1,1,1]))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

# def sumTotal(arr):
#     sum=0
#     for i in range(0,len(arr)):
#         sum=sum+arr[i]
#     return sum
# print(sumTotal([1,2,3,4]))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

# def average(arr):
#     sum=0
#     for i in range(0,len(arr)):
#         sum=sum+arr[i]
#     avg=sum/len(arr)
#     return avg
# print(average([1,2,3,4]))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

# def arrlength(arr):
#     return len(arr)
# print(arrlength([1,2,3,4]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

# def arrmin(arr):
#     return min(arr)
# print(arrmin([1,2,3,4]))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# def arrmax(arr):
#     return max(arr)
# print(arrmax([1,2,3,4]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

# def ultimateAnalyze(arr):
#     sum=0
#     dicshun={}
#     for i in range(0,len(arr)):
#         sum=sum+arr[i]
#     avg=sum/len(arr)
#     dicshun={"Sum":sum,"Avg":avg,"Minimum":min(arr),"Maximum":max(arr),"Length":len(arr)}
#     return dicshun
# print(ultimateAnalyze([1,2,3,4]))

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# def reverseList(arr):
#     temp=0
#     for i in range(0,int(len(arr)/2)):
#         temp=arr[i]
#         arr[i]=arr[len(arr)-1-i]
#         arr[len(arr)-1-i]=temp
#     return arr
# print(reverseList([1,2,3,4]))
