'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.'''

print(ord("A"))
def reverseOnlyLetters(s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1
        while(i<j):
            # Check if s[i] is a letter
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
        return ''.join(s)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))