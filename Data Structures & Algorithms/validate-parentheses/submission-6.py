class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_bracket = {'(':')','[':']','{':'}'}
        for c in s:
            if c in close_bracket:
                stack.append(close_bracket[c])
            elif not stack or stack.pop() != c:
                return False
        return not stack