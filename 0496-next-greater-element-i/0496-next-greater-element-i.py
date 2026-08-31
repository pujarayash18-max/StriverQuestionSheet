class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        nge = {}

        # Traverse nums2 from back to front
        for i in range(len(nums2) - 1, -1, -1):

            # Remove elements that cannot be the next greater
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            # Top of stack is the next greater element
            if stack:
                nge[nums2[i]] = stack[-1]
            else:
                nge[nums2[i]] = -1

            # Add current element to stack
            stack.append(nums2[i])

        # Get answers for nums1
        ans = []

        for num in nums1:
            ans.append(nge[num])

        return ans