def selectionSort(list):
    for i in range(len(list)):
        min = list[i]
        minposit = i
        for j in range(i+1, len(list)):
            if list[j] < min:
                min = list[j]
                minposit = j
                #print("Minimum is now", min)

        list[i], list[minposit] = list[minposit], list[i]
        #print("list", list[i], list[minposit], min, "has been swapped!")

    return list

print(selectionSort([1, 5, 3, 2, 0, 8, 3, 5, 3, 7, 9, 0, 5, 32, 6, 8, 32, 7, 9, 6, 4, 8, 9]))
