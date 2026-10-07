from collections import deque
from typing import List, Dict


class Solution:
    # topological sort
    # if we just follow the list of prereqs for every query there
    # are 10,000 queries times 100 courses or 1,000,000 steps total.
    # which might be ok as it's 1,000 times less than a billion.

    # Otherwise modify Course Schedule II, that produces a topological
    # sorted list of the values 0 to numCourses - 1, to produce
    # a flattened list of all prereqs for each course this might
    # require 100 prereqs for each of the 100 courses or 10,000
    # items of storage.

    # return True if there's a path from start to target
    def bfs(self, prerequisites: Dict[int, List[int]], start: int, target: int) -> bool:
        if start == target:
            return True
        seen = set([start])
        queue = deque([start])
        while queue:
            c = queue.popleft()
            if c in prerequisites:
                for n in prerequisites[c]:
                    if n == target:
                        return True
                    elif n not in seen:
                        queue.append(n)
                        seen.add(n)
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        prereqs = {}
        for a, b in prerequisites:  # a is a prereq for b
            prereqs.setdefault(b, []).append(a)  # prereq[b] = [a,]

        query_results = []
        for target, start in queries:
            query_results.append(self.bfs(prereqs, start, target))

        return query_results


numCourses=4
prerequisites=[[1,0],[2,1],[3,2]]
queries=[[0,1],[3,1]]
print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))
