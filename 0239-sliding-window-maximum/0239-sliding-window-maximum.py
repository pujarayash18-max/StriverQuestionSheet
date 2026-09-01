from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []

        for i in range(len(nums)):

            # Remove elements that are outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller or equal elements from the back
            # because they cannot be the maximum anymore
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Store the current index
            dq.append(i)

            # First complete window starts at index k - 1
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans