class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        point_left = 0
        point_right = n-1
        while  point_left <  point_right:
            while point_left <  point_right and s[point_left].isalnum() == False:
                point_left += 1
            while point_right >  point_left and s[point_right].isalnum() == False:
                point_right -=1
            if s[point_left].lower() != s[point_right].lower():
                return False
            point_left += 1
            point_right -=1
        return True
        