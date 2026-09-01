class StockSpanner:

    def __init__(self):
        # Stack stores (price, index)
        self.stack = []
        self.index = -1

    def next(self, price):
        self.index += 1

        # Remove smaller or equal prices.
        # They cannot be the previous greater element.
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        # If stack is empty, there is no previous greater element.
        # Treat its index as -1.
        if not self.stack:
            span = self.index - (-1)
        else:
            # Top of stack is the previous greater element
            previous_greater_index = self.stack[-1][1]
            span = self.index - previous_greater_index

        # Store current price and its index
        self.stack.append((price, self.index))

        return span