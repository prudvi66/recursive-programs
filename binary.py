def binarysrc(arr,start,end,y):
    if(end>=start):
        mid=(start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysrc(arr,start,mid-1,x)
        else:
            return binarysrc(arr,mid+1,end,x)
    else:
        return -1
arr=[1,2,3,4,5,6]
x=4
    
result=binarysrc(arr,0,len(arr)-1,x)
    
if(result!=-1):
        print("Element found at ",str(result))
else:
        print("Element not found in array  ",)
    
    
