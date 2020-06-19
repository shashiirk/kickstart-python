def binary_search(arr,start,end,key):
    
    while start<=end:
        mid = (start+end)//2

        if key==arr[mid]:
            return mid+1
        elif key<arr[mid]:
            end = mid-1
        else:
            start = mid+1
            
    return -1
