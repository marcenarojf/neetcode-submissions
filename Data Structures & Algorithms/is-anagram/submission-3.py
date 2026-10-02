class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1.) Create dict for both strings where 
        #key = letter 
        #value = number of occurences of that letter in word
        t_dict = {}
        s_dict = {}
        
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 0

        for letter in t:
                    if letter in t_dict:
                        t_dict[letter] += 1
                    else:
                        t_dict[letter] = 0

        print(s_dict)
        print(t_dict)
        # 2.) Compare dicts
        s_unique_letters = s_dict.keys()
        t_unique_letters = t_dict.keys()
        # 2a) compare sizes
        if len(s_unique_letters) == len(t_unique_letters):
            for letter in s_unique_letters:
                if letter in t_unique_letters:
                    if s_dict[letter] != t_dict[letter]: return False
                else: return False
            return True
        else: return False