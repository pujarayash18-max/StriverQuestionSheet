class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_value = val

        elif val >= self.min_value:
            self.stack.append(val)

        else:
            # Store encoded value
            self.stack.append(2 * val - self.min_value)
            self.min_value = val

    def pop(self):
        x = self.stack.pop()

        # Encoded value means current minimum was changed
        if x < self.min_value:
            self.min_value = 2 * self.min_value - x

    def top(self):
        x = self.stack[-1]

        # Encoded value -> actual top is min_value
        if x < self.min_value:
            return self.min_value

        return x

    def getMin(self):
        return self.min_value