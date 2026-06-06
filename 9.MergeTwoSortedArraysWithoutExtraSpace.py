class Solution:
    def merge(self, nums1, m, nums2, n):
        # Compare and swap
        for i in range(m):
            if n > 0 and nums1[i] > nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                nums2.sort()

        # Copy nums2 into remaining positions of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]

sol = Solution()
sol.merge(nums1, 3, nums2, 3)

print(nums1)