# recieve string S
# s => 1 to 100,000
# knowledge => 0 to 100,000
# only letters and lowercase?

# convert the knowledge into a dictionary
# time complexity it's linear O(m+n)

class Solution:
  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    dct_knowledge = {}
    s_result = ""
    
    for key,value in knowledge:
      dct_knowledge[key] = value

    ptr = 0
    size_s = len(s)
    while ptr < size_s:
      
      if s[ptr] == "(":
        ptr_right = ptr + 1
        
        while s[ptr_right] != ")":
          ptr_right += 1
      
        value = dct_knowledge.get(s[ptr+1:ptr_right] ,"?")
        s_result += value
        ptr = ptr_right + 1

      else:
        s_result += s[ptr]
        ptr += 1

    return s_result

# "(name)is(age)yearsold"
# 