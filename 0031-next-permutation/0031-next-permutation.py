class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find breakpoint
        index = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # Step 2: If no breakpoint, reverse the array
        if index == -1:
            nums.reverse()
            return

        # Step 3: Find the smallest element greater than nums[index]
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Step 4: Reverse the remaining part
        nums[index + 1:] = reversed(nums[index + 1:])