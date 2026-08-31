import heapq

class Solution:

    def topKFrequent(self, nums, k):
        # Count frequency of each element
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Min heap: (frequency, number)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            # Keep only k elements
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the elements
        ans = []

        while heap:
            count, num = heapq.heappop(heap)
            ans.append(num)

        return ans
object=Solution()
nums=[1,1,1,2,2,3]
k=2
print(object.topKFrequent(nums, k))