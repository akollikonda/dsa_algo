''': Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 
This problem is similar to Two Sum. (In Two Sum, the input is not sorted).'''

# this can be solved by two pointers, start at o and len(arr) add the two number and check if its gretaer or less tham sum
# if it is lesseer move the firt pointer to make sum go up and if it is greater move theright pointer to make the sum decrease/

def sorted_two_sum(arr,target):
    i = 0
    j = len(arr)-1

    while(i<j):
        if(target>arr[i]+arr[j]):
            i+=1
        elif(target<arr[i]+arr[j]):
            j-=1
        else:
            return (i,j)
    return False

print(sorted_two_sum([1, 2, 4, 6, 8, 9, 14, 15],13))

print(sorted_two_sum([1, 2, 4, 6, 8, 9, 14, 15],20))

print(sorted_two_sum([1, 2, 4, 6, 8, 9, 14, 15],300))