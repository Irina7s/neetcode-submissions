class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        current_sum = numbers[left] + numbers[right]
        while current_sum != target and left < right:
            if current_sum < target:
                left +=1
                current_sum = numbers[left] + numbers[right]
            elif current_sum >target:
                right -=1
                current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1, right+1]
        