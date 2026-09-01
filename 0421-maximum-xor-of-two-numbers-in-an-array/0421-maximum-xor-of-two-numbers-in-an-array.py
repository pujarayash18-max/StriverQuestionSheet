class Solution:
    def findMaximumXOR(self, nums):

        answer = 0
        mask = 0

        # Check bits from 30 to 0
        for bit in range(30, -1, -1):

            # Include current bit
            mask |= (1 << bit)

            prefixes = set()

            # Store prefixes up to current bit
            for num in nums:
                prefixes.add(num & mask)

            # Try making current XOR bit = 1
            candidate = answer | (1 << bit)

            found = False

            for prefix in prefixes:

                # If another prefix exists that gives candidate XOR
                if (prefix ^ candidate) in prefixes:
                    found = True
                    break

            if found:
                answer = candidate

        return answer