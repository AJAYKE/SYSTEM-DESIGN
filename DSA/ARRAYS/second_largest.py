#given minimum array size is 2

def print2largest(arr, n):
    first = arr[0]
    second = arr[1]
    
    if first<second:
        first,second = second,first
        
    for i in range(2,n):
        if arr[i] > first:
            first,second = arr[i], first
        elif (second ==first and arr[i] < first) or (arr[i] > second and arr[i]!=first):
            second = arr[i]
    if second == first:
        return -1
    return second