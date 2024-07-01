'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

def square_sort(arr):
    i = 0
    j = len(arr)-1

    while(i<j):
        if(arr[i]**2<arr[j]**2):
            j -=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            

    return [i**2 for i in arr]

print(square_sort([-4,-1,0,3,10]))
        
   
