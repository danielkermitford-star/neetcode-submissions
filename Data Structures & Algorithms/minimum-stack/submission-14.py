# not a min heap - as that would require O(lgn)

class MinStack:
        
    def __init__(self):
        self.stack = []
        self.min_so_far = []

    def push(self, val: int) -> None:
        new_min = val
        if self.min_so_far: 
            new_min = min(val, self.min_so_far[-1])
        self.min_so_far.append(new_min)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_so_far.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_so_far[-1]
