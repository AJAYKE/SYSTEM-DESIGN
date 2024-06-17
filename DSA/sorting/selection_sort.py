## Theory
# Simply put find the smallest element in the array, and interchange it with 1st element
# now do the same with array arr[1:] till end

def selectionSort(self, arr,n):
    for i in range(0,n-1):
        mini_in = i
        for j in range(i, n):
            temp = arr[j]
            if temp < arr[mini_in]:
                mini_in = j
        arr[i], arr[mini_in] = arr[mini_in], arr[i]
    
    return arr