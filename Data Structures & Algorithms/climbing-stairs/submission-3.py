class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 way to climb either 0 or 1 stairs
        number_of_ways = [1 for _ in range(n+1)] 
        for i in range(2,n+1):
            step_1 = number_of_ways[i-1]
            step_2 = number_of_ways[i-2]
            number_of_ways[i] = step_1 + step_2
        
        return number_of_ways[n]


        