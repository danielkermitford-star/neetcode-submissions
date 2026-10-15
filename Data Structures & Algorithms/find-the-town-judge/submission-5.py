from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [[] for _ in range(n + 1)]
        trusts = [[] for _ in range(n + 1)]
        for a, b in trust:
            trusted_by[b].append(a)
            trusts[a].append(b)

        count = 0
        judge = -1
        for i, people in enumerate(trusted_by):
            if len(people) == n-1 and len(trusts[i]) == 0:
                count += 1
                judge = i

        return judge if count == 1 else -1
n=4
trust=[[1,3],[4,3],[2,3]]
print(Solution().findJudge(n,trust))