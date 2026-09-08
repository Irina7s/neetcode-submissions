class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_anagram = {}

        for word in strs:
            zero_list = [0] * 26

            for char in word:
                char_index = ord(char) - ord("a")
                zero_list[char_index] += 1

            key = tuple(zero_list)

            if key in groups_anagram:
                groups_anagram[key].append(word)
            else:
                groups_anagram[key] = [word]

        return list(groups_anagram.values())
        