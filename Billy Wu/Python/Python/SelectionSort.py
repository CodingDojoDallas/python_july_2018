def selectionSort(arr):
    j=0
    i=0
    min=arr[i]
    length=len(arr)
    ind=0
    for j in range(length-j):
        for i in range(length-j):
            if arr[i]<min:
                min=arr[i]
                ind=i
        arr[j],arr[ind]=arr[ind],arr[j]
        if j > (len(arr)-2):
            return arr
        else:
            j=j+1
            i=j
            # selectionSort(arr)
            # i=j
            # ind=j
        # return arr
# j=0
# i=0
# min=arr[i]
# ind=0
# print(selectionSort([13,8,5,11,3,14,1,15,9,2,12,7,4]))
print(selectionSort([13,8,5,11,3]))