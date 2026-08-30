class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even so we can compare
            # nums[mid] with nums[mid + 1]
            if mid % 2 == 1:
                mid -= 1

            # Pair is correct, so single element is to the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                # Pair is broken, so single element is
                # at mid or somewhere to the left
                right = mid

        return nums[left]