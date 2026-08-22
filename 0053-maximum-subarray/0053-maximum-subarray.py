class Solution:
    def maxSubArray(self, nums):
        maximum = nums[0]
        total = 0

        for i in range(len(nums)):
            total = total + nums[i]

            maximum = max(maximum, total)

            if total < 0:
                total = 0

        return maximum