class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 32-bit signed integer limits
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        # 1. Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            num = num * 10 + digit

            # 4. Check 32-bit overflow
            if sign == 1 and num > INT_MAX:
                return INT_MAX

            if sign == -1 and -num < INT_MIN:
                return INT_MIN

            i += 1

        # 5. Apply sign
        return sign * num