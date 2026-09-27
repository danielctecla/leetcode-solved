# result = "ulovei"

# size -> 2

# stack = [0] -> calculate index with the size of the result
# check the size of the stack if is even don't rotate if is odd rotate
# 2 -> even pass
# 1 -> odd i have to rotate

# start is equal stack.pop
# result[start::-1] = result[start::-1]

# return result 



#            |
# ((et(oc))el)
# result = "etcoel"
# stack = [0]

# stack.push(result.size())

# when I found a close parenthesis 
# if size is odd:
#    start = stack.pop
#    result[0::-1]

class Solution:

  def reverseParentheses(self, s: str) -> str:
    result = []
    stack = []

    ptr = 0

    while ptr < len(s):
      if s[ptr] == "(":
        stack.append(len(result))
      
      elif s[ptr] == ")":
        start = stack.pop()
        result[start:] = result[start:][::-1]
        
      else:
        result.append(s[ptr])
      
      ptr += 1

    return ("").join(result)