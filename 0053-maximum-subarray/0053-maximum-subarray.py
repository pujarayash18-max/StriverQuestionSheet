class Solution:
    def maxSubArray(self, nums):
        current = maximum = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maximum = max(maximum, current)

        return maximum
obj=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(obj.maxSubArray(nums))
