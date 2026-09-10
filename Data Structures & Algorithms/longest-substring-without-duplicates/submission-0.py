class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        left = 0
        right = 0
        best_length = 0
        for i in s:
            while i in hashmap:
                hashmap.remove(s[left])
                left +=1
            hashmap.add(i)
            right +=1
            current_length = right - left
            if current_length > best_length:
                best_length = current_length
        return best_length