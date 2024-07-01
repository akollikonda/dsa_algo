'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
'''

def is_subsequence(s1,s2):
    i= j=0
    while(i<len(s1) and j<len(s2)):
        if(s1[i]==s2[j]):
            i+=1
        j+=1
    
    return i==len(s1)

print(is_subsequence("ace","abcde"))

print(is_subsequence("aec","abcde"))