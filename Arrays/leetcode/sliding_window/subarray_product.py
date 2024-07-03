'''Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]'''

def subarray_product(arr, k):
    left = ans = 0
    curr = 1
    if k <= 1:
        return 0
    for right in range(len(arr)):
        curr *= arr[right]
        while(curr>=k):
            curr//=arr[left]
            left+=1
        ans += right-left+1
    return ans

print(subarray_product([10,5,2,6],100))