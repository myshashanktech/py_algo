
# Python3 program to find min elements to
# change so array is strictly increasing
 
# Find min elements to remove from array
# to make it strictly increasing
def minRemove(arr, n):
    LIS = [0 for i in range(n)]
    len = 0
 
    # Mark all elements of LIS as 1
    for i in range(n):
        LIS[i] = 1
 
    # Find LIS of array
    for i in range(1, n):
         
        for j in range(i):
            if (arr[i] > arr[j] and (i-j)<=(arr[i]-arr[j]) ):
                LIS[i] = max(LIS[i], LIS[j] + 1)
                 
        len = max(len, LIS[i])
 
    # Return min changes for array
    # to strictly increasing
    return (n - len)
 
# Driver Code
arr = [ 1, 2, 6, 5, 4 ]
n = len(arr)
print(minRemove(arr, n))
