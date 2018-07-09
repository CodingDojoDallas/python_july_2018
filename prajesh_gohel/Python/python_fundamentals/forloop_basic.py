# 1. Basic - Print all the numbers/integers from 0 to 150.

# for i in range(1, 151):
#     print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

# for i in range(5, 1000000, 5):
#     print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

# for i in range(1, 101):
#     if(i % 5 == 0):
#         print("Coding")
#         if(i % 10 == 0):
#             print("Dojo")
#     else:
#         print(i)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# sum = 0
# for i in range(1, 500001, 2):
#     sum = sum + i
# print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).

# for i in range(2018, 0, -4):
#     print(i)

# 6. Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)

# def countdown(lowNum, highNum, mult):
#     for i in range(lowNum, highNum):
#         if(i % mult == 0):
#             print(i)
# countdown(2, 10, 3)

# Predict the output for the following codes:

# list = [3,5,1,2]
# for i in list:
#     print(i)

#Prediction: 3, 5, 1, 2
#Answer: 3, 5, 1, 2

# list = [3,5,1,2]
# for i in range(list):
#     print(i)

#Prediction: 1, 2, 3, 5
#Answer: error object can't be interpreted as integer

# list = [3,5,1,2]
# for i in range(len(list)):
#     print(i)

#Prediction: 0, 1, 2, 3
#Output: 0, 1, 2, 3

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)

a()
