# Basic - Print all numbers from 0 to 150

# for count in range (151):
# 	print (count)

# Multiples of 5 - Print all the Multiples of 5 from 5 to one million

# for count in range (1000001):
# 	if count % 5 ==0:
# 		print (count)

# Counting, the Dojo Way

# for count in range (1,101):
# 	if count % 10 ==0:
# 		print("CodingDojo")
# 	elif count % 5 == 0:
# 		print("Coding")
# 	else:
# 		print(count)

# Whoa, That Sucker's Huge - Add odd integers from 0 to 500,000, and print final sum
# sum = 0
# for count in range (0,500000):
# 	if count % 2 != 0:
# 		sum = sum+count
# print(sum)

# Countdown by Fours Print positive integers starting at 2018 by 4, do not include 0
# for count in range (2018, 0, -1):
# 	if count % 4 == 0:
# 		print(count)

# Flexible Countdown - Based on Countdown... given low Num, High Num, mult, print multiples of mult from lowNum to highNum
lowNum = 2
highNum = 9
mult = 3
for count in range (lowNum,highNum+1):
	if count % mult == 0:
		print (count)