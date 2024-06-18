# Theory
# Basically we will select a pivot and iterate throw the array
# we will push all values < pivot to its left and > to its right
# Now how we do it is lil complex

def quickSort(self,arr,low,high):
    if low>high:
        return
    self.partition(arr,low,high)
    
    return arr
                    
def partition(self,arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        while arr[i] <= pivot and i <=high-1:
            i += 1
        
        while arr[j] > pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    
    self.quickSort(arr,low,j-1)
    self.quickSort(arr,j+1,high)