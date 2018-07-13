
def bubbleSort(arr):
    count=0
    for i in range(len(arr)-1-count):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        count=count+1
    # if count<(len(arr)/2):
    #     bubbleSort(arr)
    # else:
    return arr
print(bubbleSort([10,5,11,3,14,8,4,9,2,12,7,15]))