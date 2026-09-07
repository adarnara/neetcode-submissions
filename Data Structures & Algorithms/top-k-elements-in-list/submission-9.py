class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        count_nums = dict()

        min_heap = [num for num in nums]


        heapq.heapify(min_heap)

        for num in min_heap:

            if str(num) not in count_nums:
                count_nums[str(num)] = 1
            else:
                count_nums[str(num)] += 1
            
        
        return [int(x) for x in sorted(count_nums, key=lambda x: count_nums[x], reverse=True)[:k]]
        '''

        '''
        #could be done with collections.Counter.
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        
        min_heap = []

        for num,freq in count_map.items():

            heapq.heappush(min_heap, (freq, num))

            # If heap exceeds size k, drop the element with the lowest frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return [num for _, num in min_heap]

        # this is O(nlogk) there is even faster with bucket sort O(n)
        '''

        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count_map.items():
            buckets[freq].append(num)
        
        res = list()

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
#edge case to ask interviewer for this question is what do we do in the case of ties of same k frequency? 
        














        


        