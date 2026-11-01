class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        especial_char = ["*","#","%"]
        for element in s:
            if element not in especial_char:
                ans.append(element)
                continue

            if element == "*" and ans:
                ans.pop()
            elif element == "#":
                ans.extend(ans.copy())
            elif element == "%":
                ans = ans[::-1]
                

        result = ""
        return "".join(ans)