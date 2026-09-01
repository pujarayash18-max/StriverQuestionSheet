class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            x = ord(s[i]) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for i in range(n):
            x = ord(s[i]) - ord('a')

            if first[x] != i:
                continue

            left = i
            right = last[x]
            j = left
            valid = True

            while j <= right:
                x = ord(s[j]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                j += 1

            if valid:
                intervals.append([left, right])

        def get_end(interval):
            return interval[1]

        intervals.sort(key=get_end)

        ans = []
        end = -1

        for left, right in intervals:
            if left > end:
                ans.append(s[left:right + 1])
                end = right

        return ans