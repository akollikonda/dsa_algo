# Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

# We will use two pointers in this one for each array and we will iterate and compare each element in each array then merge

def sort_and_merge(arr1, arr2):
    i=j=0
    sorted_arr = []

    while (i<len(arr1) and j<len(arr2)):
        if(arr1[i]<arr2[j]):
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    
    return sorted_arr


print(sort_and_merge([1,4,10],[2,4,7]))
