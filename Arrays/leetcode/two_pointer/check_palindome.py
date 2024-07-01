'''Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".'''

def check_palindome(s):
    '''Two pointers one start at the start of string and other at end of string'''
    i = 0
    j = len(s)-1

    # Move the pointer towards each other checking each letter

    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True

print(check_palindome("abcdcba"))

print(check_palindome("racecar"))

print(check_palindome("Abhilash"))