'''Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.'''

def find_best_subarray(arr,k):
    curr = 0

    for i in range(k):
        curr +=arr[i]
    
    ans = curr

    for i in range(k,len(arr)):
        curr += arr[i]-arr[i-k]
        ans = max(ans,curr)

    return ans

print(find_best_subarray([3,-1,4,12,-8,5,6],4))