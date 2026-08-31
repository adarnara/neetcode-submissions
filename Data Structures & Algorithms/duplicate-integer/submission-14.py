class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dup = set()

        for i in range(len(nums)):
            dup.add(nums[i])
        
        if len(dup) < len(nums):
            return True
            
        return False
        

#two pointer could work too (but only on sorted arrays, unsorted wont capture)
    '''
    nums.sort()

    start = 0
    end = 1

    while end < len(nums):
        if nums[start] == nums[end]:
            return True

        start += 1
        end += 1

    return False
    '''