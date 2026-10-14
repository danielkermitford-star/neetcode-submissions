from math import inf
from typing import List


class Solution:
    # with at most k stops is setting us up to use the Bellman-Ford algorithm
    # Using Dijkstra's would require finding the shortest path with at most j stops for every
    # j <= k.  But this is exactly what Bellman-Ford's algorithm does!  So adapting Dijkstra's
    # just makes it more complicated and slower.

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # neighbors_of = [[] for _ in range(n)]


        cheapest_price_with_i_layovers_to = [inf for _ in range(n)]

        # calculate the cheapest prices without any layovers
        for (origin, destination, price) in flights:
            if origin == src:
                cheapest_price_with_i_layovers_to[destination] = price

        # calculate the cheapest prices with 1 to k layovers
        for i in range(1,k+1):
            cheapest_price_with_one_more_layover_to = [inf for _ in range(n)]
            for (origin, destination, price) in flights:
                cheapest_price_with_one_more_layover_to[destination] = min(cheapest_price_with_i_layovers_to[destination], cheapest_price_with_one_more_layover_to[destination], cheapest_price_with_i_layovers_to[origin] + price)
            cheapest_price_with_i_layovers_to = cheapest_price_with_one_more_layover_to

        if cheapest_price_with_i_layovers_to[dst] < inf:
            return cheapest_price_with_i_layovers_to[dst]
        else:
            return -1

n=4
flights=[[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
src=0
dst=3
k=1
n=5
flights=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src=2
dst=1
k=1
n=3
flights=[[0,1,2],[1,2,1],[2,0,10]]
src=1
dst=2
k=1
print(Solution().findCheapestPrice(n,flights,src,dst,k))

