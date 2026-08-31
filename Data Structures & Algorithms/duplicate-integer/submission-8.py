class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for i in range(len(nums)):
            dup.add(nums[i])
        
        if len(dup) < len(nums):
            return True
            
        return False

#two pointer could work too
        
        start = 0
        end = 1

        while start < end and end != len(nums) - 1:
            if nums[start] == nums[end]:
                return True
            start = start + 1
            end = end + 1
        return False