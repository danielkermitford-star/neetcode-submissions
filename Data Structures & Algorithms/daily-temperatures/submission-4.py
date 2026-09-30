class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # use a stack of non-ascending (i, temperature) pairs 
        # where the next warmer temperature hasn't been
        # found yet
        stack = []  
        for i, t in enumerate(temperatures):
            while stack:
                i2 = stack[-1]
                if t > temperatures[i2]:
                    stack.pop()
                    result[i2] = i - i2
                else:
                    break
            stack.append(i)
        
        return result