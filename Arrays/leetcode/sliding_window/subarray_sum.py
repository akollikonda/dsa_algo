'''Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.'''

def longest_sub_array(arr,k):
    left = curr = ans = 0

    for right in range(len(arr)):
        curr += arr[right]
        while(curr>k):
            curr-=arr[left]
            left+=1
        ans = max(ans,right-left+1)
    return ans


print(longest_sub_array([3, 1, 2, 7, 4, 2, 1, 1, 5],25))
        
