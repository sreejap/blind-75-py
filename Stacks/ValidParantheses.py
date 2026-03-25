class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ')': '(' , '}':'{' , ']':'[' } # this is using the opposite mapping, we could also map ( -> )
        stack = []
        for c in s: # var is s
            if c in mapping:
                # pop and check
                if stack:
                    pair = stack.pop() # (
                    if mapping [c] != pair:
                        return False
                else:
                    stack.append('#')
            else:
                stack.append(c) # (
        
        return len (stack) == 0       

## the other way
# def is_valid_parantheses (s):
# 	if not s:
# 	 return False
#     	stack = []
#         pairing = {"(":")", "[":"]","{":"}"} # "{[()]}"
	
# 	for c in s:
# 	  if c in pairing:
# 	    stack.append (c) # assuming we have all valid chars in the string
#           else:
# 	    pair = stack.pop()
# 	    if not stack or pairing[pair] != c:  ## add the empty check
# 		return False
        
# 	return len(stack) == 0 ; we have to check if stack is empty
