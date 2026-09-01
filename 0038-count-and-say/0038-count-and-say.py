class Solution:
    def countAndSay(self, n):
        ans = "1"

        for _ in range(n - 1):
            new = ""
            i = 0

            while i < len(ans):
                count = 1

                # Count consecutive same digits
                while i + 1 < len(ans) and ans[i] == ans[i + 1]:
                    count += 1
                    i += 1

                # Add count + digit
                new += str(count) + ans[i]

                i += 1

            ans = new

        return ans