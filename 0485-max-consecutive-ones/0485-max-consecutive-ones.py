class Solution():
    def findMaxConsecutiveOnes(self,nums):
        best = cur = 0
        for x in nums:
            cur = cur + 1 if x == 1 else 0
            best = max(best, cur)
        return best