class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        current_window = 0
        max_count = 0
        max_window = 0
        char_dict = {}
        while right < len(s):
            char_dict[s[right]] = 1 + char_dict.get(s[right], 0)
            max_count = max(max_count, char_dict[s[right]])
            current_window = right - left + 1
            k_need = current_window - max_count
            while k_need > k:
                   char_dict [s[left]] -= 1
                   left += 1
                   current_window = right - left + 1
                   k_need = current_window - max_count
            if current_window > max_window:
                   max_window = current_window
            right += 1
        return max_window
        