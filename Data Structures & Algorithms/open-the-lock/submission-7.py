from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        setofdeadends = set(tuple(int(d) for d in combo) for combo in deadends)
        target_as_ints = tuple(int(d) for d in target)
        start = (0, 0, 0, 0)
        movesfromstart = {start: 0}
        queue = deque([start])  # everything in the queue must also be in movesfromstart
        while queue:
            combo = queue.popleft()
            if combo in setofdeadends:
                continue

            # everything in the queue must also be in movesfromstart
            n_moves = movesfromstart[combo]
            if combo == target_as_ints:
                return n_moves

            for i, digit in enumerate(combo):
                for new_digit in (digit - 1) % 10, (digit + 1) % 10:
                    comboaslist = list(combo)
                    comboaslist[i] = new_digit
                    new_combo = tuple(comboaslist)
                    if new_combo not in movesfromstart:
                        movesfromstart[new_combo] = 1 + n_moves
                        queue.append(new_combo)
                        # everything in the queue must also be in movesfromstart
        return(-1)
deadends = ["1111","0120","2020","3333"]
target = "5555"
deadends=["4443","4445","4434","4454","4344","4544","3444","5444"]
target ="4444"
print(Solution().openLock(deadends, target))