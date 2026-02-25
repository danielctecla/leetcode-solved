class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mapW1 = {}
        mapW2 = {}

        for letter in word1:
            if letter in mapW1:
                mapW1[letter] += 1
            else:
                mapW1[letter] = 1
        
        for letter in word2:
            if letter in mapW2:
                mapW2[letter] += 1
            else:
                mapW2[letter] = 1
        
        return (mapW1.keys() == mapW2.keys()) and (sorted(mapW1.values()) == sorted(mapW2.values()))
