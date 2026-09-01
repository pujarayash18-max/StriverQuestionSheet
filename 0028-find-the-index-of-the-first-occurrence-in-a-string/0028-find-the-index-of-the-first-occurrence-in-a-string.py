class Solution:
    def strStr(self, haystack, needle):

        # Create combined string
        s = needle + "#" + haystack

        n = len(s)
        z = [0] * n

        left = right = 0

        # Build Z array
        for i in range(1, n):

            if i <= right:
                z[i] = min(right - i + 1, z[i - left])

            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > right:
                left = i
                right = i + z[i] - 1

        # Search for complete needle
        for i in range(len(needle) + 1, n):
            if z[i] == len(needle):
                # Convert combined-string index to haystack index
                return i - len(needle) - 1

        return -1