class Solution:
    def isValid(self, s):

        stack = []

        for ch in s:

            # Opening brackets
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            # Closing brackets
            else:

                # No opening bracket to match
                if not stack:
                    return False

                top = stack.pop()

                # Check matching pair
                if ch == ')' and top != '(':
                    return False

                if ch == ']' and top != '[':
                    return False

                if ch == '}' and top != '{':
                    return False

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0