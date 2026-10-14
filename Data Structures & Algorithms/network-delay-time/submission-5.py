import heapq
from math import inf
from typing import List


class Solution:
    # straightforward application of Dijkstra's Algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors_of = [[] for _ in range(n+1)]
        for u, v, t in times:
            neighbors_of[u].append((v,t))

        min_heap = [(0,k)]
        # heapq.heapify(min_heap)
        time_to_send_signal_to = [inf for _ in range(n+1)]
        finalized = [False for _ in range(n+1)]
        # print (time_to_send_signal_to_k)

        while min_heap:
            time_to_v, v = heapq.heappop(min_heap)
            if not finalized[v]:
                finalized[v] = True
            # if time_to_v < time_to_send_signal_to[v]:
                # time_to_send_signal_to[v] = time_to_v
                n -= 1  # one less node to the signal needs to reach
                if n == 0:   # no more nodes need to reach the signal
                    return time_to_v
                for u, time_from_v_to_u in neighbors_of[v]:
                    time_to_v_then_u = time_to_v + time_from_v_to_u
                    if time_to_v_then_u < time_to_send_signal_to[u]:
                        time_to_send_signal_to[u] = time_to_v_then_u
                        heapq.heappush(min_heap, (time_to_v_then_u, u))
        return -1

times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
n = 4
k = 1
times=[[2,1,1],[2,3,1],[3,4,1]]
n=4
k=2
times=[[1,2,1],[2,3,1]]
n=3
k=2
print(Solution().networkDelayTime(times, n, k))