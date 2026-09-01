class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()

        # Keep original query index
        queries = sorted(
            [(m, x, i) for i, (x, m) in enumerate(queries)]
        )

        # Binary Trie using arrays
        # left/right store child node indices
        left = [-1]
        right = [-1]

        def insert(num):
            node = 0

            for bit in range(30, -1, -1):
                b = (num >> bit) & 1

                if b == 0:
                    if left[node] == -1:
                        left[node] = len(left)
                        left.append(-1)
                        right.append(-1)

                    node = left[node]

                else:
                    if right[node] == -1:
                        right[node] = len(left)
                        left.append(-1)
                        right.append(-1)

                    node = right[node]

        def get_max_xor(num):
            node = 0
            result = 0

            for bit in range(30, -1, -1):
                b = (num >> bit) & 1

                # Prefer opposite bit
                if b == 0:
                    if right[node] != -1:
                        result |= (1 << bit)
                        node = right[node]
                    else:
                        node = left[node]
                else:
                    if left[node] != -1:
                        result |= (1 << bit)
                        node = left[node]
                    else:
                        node = right[node]

            return result

        ans = [-1] * len(queries)
        j = 0

        for m, x, index in queries:

            # Insert all numbers <= m
            while j < len(nums) and nums[j] <= m:
                insert(nums[j])
                j += 1

            if j > 0:
                ans[index] = get_max_xor(x)

        return ans