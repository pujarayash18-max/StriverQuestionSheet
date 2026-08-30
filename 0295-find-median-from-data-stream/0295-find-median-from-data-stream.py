import heapq

class MedianFinder:

    def __init__(self):
        # Max heap for the smaller half
        # Python has only min heap, so store negative values
        self.left = []

        # Min heap for the larger half
        self.right = []

    def addNum(self, num):

        # Step 1: Add number to left (max heap)
        heapq.heappush(self.left, -num)

        # Step 2: Make sure every element in left <= every element in right
        if self.right and -self.left[0] > self.right[0]:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        # Step 3: Balance the sizes
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self):

        # Odd number of elements
        if len(self.left) > len(self.right):
            return -self.left[0]

        # Even number of elements
        return (-self.left[0] + self.right[0]) / 2.0