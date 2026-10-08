class Solution:
    def bfs(self, i: int, neighbors_of: List[List[int]], seen: Set[int]):
        queue = deque([i])
        while queue:
            i = queue.popleft()
            if i in seen:
                continue
            seen.add(i)
            for n in neighbors_of[i]:
                queue.append(n)


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors_of = [[] for _ in range(n)]
        for i,j in edges:
            neighbors_of[i].append(j)
            neighbors_of[j].append(i)

        n_connected = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                n_connected += 1
                self.bfs(i, neighbors_of, seen)
        return n_connected