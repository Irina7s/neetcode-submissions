class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        window_count = {}
        window_length = len(s1)
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1) - 1
        for i in s1:
            s1_count[i] = 1+ s1_count.get(i, 0)
        for j in range(0, len(s1)):
            window_count[s2[j]] = 1 + window_count.get(s2[j], 0)
        if window_count == s1_count:
            return True
        while len(s2) > right + 1:
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:     
                window_count.pop(s2[left])
            left += 1
            right += 1
            window_count[s2[right]] = 1 + window_count.get(s2[right], 0)
            if window_count == s1_count:         
                return True
        return False
        