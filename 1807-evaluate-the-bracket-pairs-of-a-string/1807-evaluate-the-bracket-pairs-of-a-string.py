# recieve string S
# s => 1 to 100,000
# knowledge => 0 to 100,000
# only letters and lowercase?

# convert the knowledge into a dictionary
# time complexity it's linear O(m+n)

class Solution:
  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    s_result = ""
    dct_knowledge = dict(knowledge)

    i = 0
    while i < len(s):
      
      if s[i] == "(":
        j = s.find(")", i + 1)
      
        value = dct_knowledge.get(s[i+1:j] ,"?")
        s_result += value
        i = j + 1

      else:
        s_result += s[i]
        i += 1

    return s_result

# "(name)is(age)yearsold"
# 