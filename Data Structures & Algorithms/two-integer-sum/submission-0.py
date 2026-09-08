class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(len(nums)):
            need_number = target - nums[i]

            if need_number in seen:
                return [seen.get(need_number), i] 
            else:     
                seen[nums[i]]=i