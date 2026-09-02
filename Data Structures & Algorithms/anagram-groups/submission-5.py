class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_mapping = dict()

        for word in strs:
            char_frequency = [0] * 26

            for char in word:
                char_frequency[ord(char) - ord('a')] += 1
            
            key = tuple(char_frequency)
            if key not in anagram_mapping:
                anagram_mapping[key] = []
            anagram_mapping[key].append(word)

        return list(anagram_mapping.values())



        