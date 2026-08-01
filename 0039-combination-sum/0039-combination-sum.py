class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)  # Reuse same element
                path.pop()  # Backtrack

        backtrack(0, target, [])
        return result