'''
A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same 
forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome,
or false otherwise.
'''

def isPalindrome(s: str) -> bool:
    # # Two pointers from each end of a filtered string
    # # T: O(s/2) S: O(1)

    # # Filter only alphabetic characters and make them lowercase
    # s = ''.join(filter(str.isalnum, s)).lower()

    # length = len(s)
    # for i in range(length // 2):
    #     if s[i] != s[length - 1 - i]: return False
    # return True



    # Two pointers on the original string
    
    i = 0
    j = len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower(): return False
        i += 1
        j -= 1
    return True
