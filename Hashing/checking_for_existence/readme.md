#  Checking for existence

One of the most common applications of a hash table or set is determining if an element exists in 
𝑂
(
1
)
O(1). Since an array needs 
𝑂
(
𝑛
)
O(n) to do this, using a hash map or set can improve the time complexity of an algorithm greatly, usually from 
𝑂
(
𝑛
2
)
O(n 
2
 ) to 
𝑂
(
𝑛
)
O(n). Let's look at some example problems.

Example 1: 1. Two Sum

Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

The brute force solution would be to use a nested for loop to iterate over every pair of indices and check if the sum is equal to target. This will result in a time complexity of 
𝑂
(
𝑛
2
)
O(n 
2
 ). In the brute force solution, the first for loop focuses on a number num and does a second for loop which looks for target - num in the array. With an array, looking for target - num is 
𝑂
(
𝑛
)
O(n), but with a hash map, it is 
𝑂
(
1
)
O(1).

We can build a hash map as we iterate along the array, mapping each value to it's index. At each index i, where num = nums[i], we can check our hash map for target - num. Adding key-value pairs and checking for target - num are all 
𝑂
(
1
)
O(1), so our time complexity will improve to 
𝑂
(
𝑛
)
O(n).
```class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]
```

If the question wanted us to return a boolean indicating if a pair exists or to return the numbers themselves, then we could just use a set. However, since it wants the indices of the numbers, we need to use a hash map to "remember" what indices the numbers are at.

Example 2: 2351. First Letter to Appear Twice

Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.

The brute force solution would be to iterate along the string, and for each character c, iterate again up to c to see if there is any match.

```
    class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c

        return ""
```
This is 
𝑂
(
𝑛
2
)
O(n 
2
 ) due to the nested loop. The second loop is checking for the existence of c, which can be done in 
𝑂
(
1
)
O(1) using a set.


```
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "
```

This improves our time complexity to 
𝑂
(
𝑛
)
O(n) as each for loop iteration now runs in constant time.

The space complexity is a more interesting topic of discussion. Many people will argue that the space complexity is 
𝑂
(
1
)
O(1) because the input can only have characters from the English alphabet, which is bounded by a constant (26). This is very common with string problems and technically correct. In an interview setting, this is probably a safe answer, but you should also note that the space complexity could be 
𝑂
(
𝑚
)
O(m), where 
𝑚
m is the number of allowable characters in the input. This is a more general answer and also technically correct.

--------------

Example 3: Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

We can solve this in a straightforward manner - just iterate through nums and check if x + 1 or x - 1 is in nums. By converting nums into a set beforehand, these checks will cost 
𝑂
(
1
)
O(1).

Converting the input into a set beforehand is another example of pre-processing.

```
def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)
    
    return ans
```


Because the checks are 
𝑂
(
1
)
O(1), the time complexity is 
𝑂
(
𝑛
)
O(n) since each for loop iteration runs in constant time. The set will occupy 
𝑂
(
𝑛
)
O(n) space.

## Anytime you find your algorithm running if ... in ..., then consider using a hash map or set to store elements to have these operations run in 𝑂(1) O(1). 