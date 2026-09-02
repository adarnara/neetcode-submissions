class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_mapping = dict()

        for word in strs:
            char_frequency = [0] * 26

            for char in word.lower():
                char_frequency[ord(char) - ord('a')] += 1
            
            key = tuple(char_frequency)
            if key not in anagram_mapping:
                anagram_mapping[key] = []
            anagram_mapping[key].append(word)

        return list(anagram_mapping.values())

# an interesting thought, this problem doesnt specifiy case sensitivity which is why we should ask do we assume input will all be lowercase? if not we need to extend char_frequency from [0] * 26 to 52 for upper case (26*2 = 52).


        