class Solution:
    def reverseWords(self, s):
        # Split into words and ignore extra spaces
        words = s.split()

        # Reverse the words and join with one space
        return " ".join(words[::-1])