class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        # Add 0 at the end to process all remaining bars
        heights.append(0)

        for i in range(len(heights)):

            # Current bar is smaller, so calculate areas
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]

                # If stack is empty, rectangle starts from index 0
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                area = h * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area