# 1. Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

# def biggieSize(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] = "big"
#
#     return list
#
# print(biggieSize([-2, -1, 1, 2]))

# 2. Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).

# def countPositives(list):
#     count = 0
#     for i in range(len(list)):
#         if list[i] > 0:
#             count += 1
#
#     list[len(list)-1] = count
#     return list
#
# print(countPositives([-1, 1, 1, 1]))

# 3. SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10

# def sumTotal(list):
#     sum = 0
#     for i in range(len(list)):
#         sum = sum + list[i]
#
#     return sum
#
# print(sumTotal([1, 2, 3, 4]))

# 4. Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5

# def average(list):
#     sum = 0
#     for i in range(len(list)):
#         sum = sum + list[i]
#
#     avr = sum/len(list)
#     return avr
#
# print(average([2, 4, 6, 8]))

# 5. Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4

# def length(list):
#     count = 0
#     for i in list:
#         count += 1
#
#     return count
#
# print(length([3, 5, 2, 4, 4]))

# 6. Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

# def minimum(list):
#     min = list[0]
#     for i in range(len(list)):
#         if list[i] < min:
#             min = list[i]
#
#     return min
#
# print(minimum([4, 6, 2, 4, 3, 7]))

# 7. Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

# def maximum(list):
#     max = list[0]
#     for i in range(len(list)):
#         if list[i] > max:
#             max = list[i]
#
#     return max
#
# print(maximum([4, 6, 2, 4, 3, 7]))

# 8. UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

# def UltimateAnalyze(list):
#     sum = 0
#     min = list[0]
#     max = list[0]
#     count = 0
#     d = {}
#     for i in list:
#         if i < min:
#             min = i
#
#         if i > max:
#             max = i
#
#         sum = sum + i
#         count += 1
#
#     avr = sum/count
#     d["sumTotal"] = sum
#     d["Average"] = avr
#     d["Minimum"] = min
#     d["Maximum"] = max
#     d["Length"] = count
#     return d
#
# print(UltimateAnalyze([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

# def reverseList(list):
#     temp = 0
#     for i in range(int(len(list)/2)):
#         temp = list[i]
#         list[i] = list[len(list) - 1 - i]
#         list[len(list) - 1 -i] = temp
#
#     return list
#
# print(reverseList([2, 4, 6, 8, 10]))
