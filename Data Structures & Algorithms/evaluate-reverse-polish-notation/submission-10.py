class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = set(['+','-','*','/'])
        for t in tokens:
            if t in operators:
                # 2nd_last t last
                b = operands.pop()
                a = operands.pop()
                match t:
                    case '+':
                        operands.append(a+b)
                    case '-':
                        operands.append(a-b)
                    case '*':
                        operands.append(a*b)
                    case '/':
                        # Python's // is floor division
                        # problem specifies truncate toward 0
                        c = a // b
                        if c < a / b < 0:
                            c += 1
                        operands.append(c)
            else:
                operands.append(int(t))
        return operands.pop()        