from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_counts_s = dict()
        char_counts_t = dict()

        for i in s:
            if i not in char_counts_s:
                char_counts_s[i] = 1
            
            char_counts_s[i] += 1
        
        for i in t:
            if i not in char_counts_t:
                char_counts_t[i] = 1
            
            char_counts_t[i] += 1
        
        s_counter = Counter(char_counts_s)
        t_counter = Counter(char_counts_t)

        return s_counter == t_counter

        


        