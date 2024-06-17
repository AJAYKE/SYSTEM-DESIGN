## Theory
# It is similar to selection sort but reverse. Here we will get the maximum element first
# and put it at the end of the array, then find the max_element of arr[:-1] and repeat it.

def bubbleSort(self,arr, n):
    for i in range(n-1,-1,-1):
        max_in = i
        for j in range(0,i):
            if arr[j] > arr[max_in]:
                max_in = j
        arr[i], arr[max_in] = arr[max_in], arr[i]
    return arr