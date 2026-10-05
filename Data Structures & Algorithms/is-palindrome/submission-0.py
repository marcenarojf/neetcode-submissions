class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Parse to only alphanumerics
        s_parsed = []
        # .lower for case insensitiveness
        for char in s.lower():
            if char.isalnum(): s_parsed.append(char)

        s_size = len(s_parsed) # size of for
        nth_element = s_size-1 #last element
        Palindrome = True 

        for i in range(0,s_size):
            j = nth_element - i # 1st char vs last char, 2nd vs 2nd to last and so on...
            if s_parsed[i] != s_parsed[j]: Palindrome = False 
 
        return Palindrome