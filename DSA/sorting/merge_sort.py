#solution1 with passing two arrays

def merge(arr1, arr2):
    if len(arr1) > 1:
        arr1 = mergeSort(arr1,0, len(arr1))

    if len(arr2) > 1:
        arr2 = mergeSort(arr2,0, len(arr2))
    
    l = 0
    r = 0
    res = []
    
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            res.append(arr1[l])
            l += 1
        else:
            res.append(arr2[r])
            r += 1
    if l < len(arr1):
        res.extend(arr1[l:])
    
    if r < len(arr2):
        res.extend(arr2[r:])
    return res
        
def mergeSort(arr, l, r):
    m = r//2
    arr1 = arr[l:m]
    arr2 = arr[m:r]
    
    arr = merge(arr1,arr2)
    
    # print(arr1, arr2, arr)
    
    return arr


#solution2 editing the array inplace

class Solution:
    def merge(self,arr, l, m, r): 
        i = l
        j = m+1
        temp = []
        
        while i<=m and j<=r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j+= 1
        
        while i<=m:
            temp.append(arr[i])
            i += 1
        while j<=r:
            temp.append(arr[j])
            j+= 1
        
        for i in range(l,r+1):
            arr[i] = temp[i-l]
            
    def mergeSort(self,arr, l, r):
        if l == r:
            return
        m = (l+r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m+1,r)
        self.merge(arr,l,m,r)
