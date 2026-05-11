# https://leetcode.com/problems/basic-calculator/
# https://www.youtube.com/watch?v=A3noAzWZ9f4&t=311s
class Solution:
    def calculate(self, s: str) -> int:
        output, curr, sign, stack = 0, 0, 1, []

        for c in s:
            if c.isdigit():
                curr = curr * 10 + int (c)
            elif c in "+-":
                output += (curr*sign)
                curr = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(output)
                stack.append(sign)
                # reset here
                output = 0
                sign = 1
            elif c == ")":
                output += (curr*sign) # caclulate the current output
                output *= stack.pop() # add the remaining from stack
                output += stack.pop()
                curr = 0
            
        return output + (curr*sign)
