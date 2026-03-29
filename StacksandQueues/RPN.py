class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operands = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in operands:
                stack.append(int(t))           # important to convert here 
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == "+":
                    ans = n1 + n2
                elif t == "-":
                    ans = n2 - n1
                elif t == "*":
                    ans = n1 * n2
                else:
                    ans = int (n2 /n1)
                stack.append(ans)

        res = stack.pop()
        return res
        
