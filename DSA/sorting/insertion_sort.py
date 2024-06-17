## Theory
# lets start with single element array, then keep on adding one element and 
# adjust the position of new element in its respective appropriate position

def insertionSort(self, alist, n):
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    
    return alist