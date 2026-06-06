class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find entrance of cycle
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
nums = [1, 3, 4, 2, 5]
sol = Solution()
print(sol.findDuplicate(nums))