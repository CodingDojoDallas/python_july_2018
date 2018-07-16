# Biggie Size
# def makeitbig(arr):
# 	for i in range (len(arr)):
# 		if arr[i] > 0:
# 			arr[i] = "big"
# 	return arr

# z=makeitbig([1,-5,3,4,-8])

# print(z)

# Count Positives
# def countpos(arr):
# 	count = 0
# 	for i in range (len(arr)):
# 		if arr[i] > 0:
# 			count = count+1
# 	# return count
# 	arr[len(arr)-1]=count
# z=countpos([1,-5,3,4,-8])
# print(z)

# SumTotal
# def total(arr):
# 	sum = 0
# 	for i in range (len(arr)):
# 		sum = sum + arr[i]
# print(total([1,3,5])

# Average
# def aver(arr):
# 	sum = 0
# 	ave = sum/len(arr)
# 	for i in range (len(arr)):
# 		sum = sum + arr[i]
# 	print(ave)
# aver([1,2,3])

# length
# def leng(arr):
# 	print(len(arr))
# leng([1,2,3,4,5])

# Minimum

# def minn(arr):
# 	mini = arr[0]
# 	for i in range (len(arr)):
# 		if arr[i] < mini:
# 			mini = arr[i]
# 	print(mini)
# minn([1,2,5,-5])

# Maximum
# def maximum(arr):
# 	maxi = arr[0]
# 	for i in range (len(arr)):
# 		if arr[i] > maxi:
# 			maxi = arr[i]
# 	print(maxi)
# maximum([1,2,8,4,5])

# Ultimate Analze
# def toDict(arr):
# 	sumd = 0
# 	mind = arr[i]
# 	maxd = arr[i]
# 	for i in range (len(arr)):
# 		if arr[i]<min:
# 			min=arr[i]
# 		if arr[i]>max:
# 			max=arr[i]
# 		sum=sum+arr[i]
# 	print dict{'sum': sumd, 'avg' : sumd/arr(len), 'min' : mind, 'max' : maxd, 'length' : arr(len)}
# 	

# ReverseList
# def rever(arr):
# 	temp = arr[0]
# 	for i in range (int(len(arr)/2)):
# 		arr[i] = arr[len(arr)-(i+1)]
# print(rever([1,2,4,5,8]))