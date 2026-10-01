class Solution:
    def time_required(self, piles:List[int], k: int) -> int:
        time = 0
        for bananas in piles:
            time += math.ceil(bananas / k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)  # guaranteed to be large enough
        min_k = 1           # might be too small
        while min_k < max_k:
            mid_k = (max_k + min_k) // 2  
            # truncates remainder => mid_k < max_k
            if self.time_required(piles, mid_k) > h:  # takes too long
                min_k = mid_k + 1
            else:
                max_k = mid_k   # might be the best: mid_k < max_k
        return max_k