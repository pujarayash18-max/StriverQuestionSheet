class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs:
                # Stop if this position doesn't exist
                # or the character is different
                if i >= len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix