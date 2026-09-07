class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = dict()

        min_heap = [num for num in nums]


        heapq.heapify(min_heap)

        for num in min_heap:

            if str(num) not in count_nums:
                count_nums[str(num)] = 1
            else:
                count_nums[str(num)] += 1
            
        
        return [int(x) for x in sorted(count_nums, key=lambda x: count_nums[x], reverse=True)[:k]]






        


        