class Solution:
    def isAnagram(self, s, t):

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        count = [0] * 26

        # Count characters from s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Remove characters using t
        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        # Every frequency should become 0
        for x in count:
            if x != 0:
                return False

        return True