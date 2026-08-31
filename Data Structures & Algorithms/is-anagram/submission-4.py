from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #return Counter(s) == Counter(t) #easiest way but probably not allowed

        if len(s) != len(t): #case where strings arent same length
            return False

        char_counts = dict()


        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        for char in t:
            char_counts[char] = char_counts.get(char, 0) - 1

        for count in char_counts.values():
            if count != 0:
                return False

        return True

        # OR with two dicts:

        '''
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
        '''



        


        