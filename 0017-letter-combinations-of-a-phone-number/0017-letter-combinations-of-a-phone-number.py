class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # create the dictionary
        
        # use a stack
        # fill the stack pushing each element of the first digit
        # result variable list
        # while stack
        #     pop element
            
        #     verify if element is equal to len of the digits
        #         yes append to result
        #     else:
        #         index = len of element - 1
        #         then
        #         for s in dictionary[digits[index + 1]]
        #             stack.append(element + [s])
        # return result
        
        # time complexity O(3^n)
        # memory complexity(3^n)

        # This is my approach 

        phone_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        stack = []
        result = []
        number_digits = len(digits)

        for letter in phone_letters[digits[0]]:
            stack.append(letter)

        while stack:
            combination = stack.pop()
            comb_size = len(combination)
            if comb_size == number_digits:
                result.append(combination)
            else:
                index = comb_size - 1 # getting the real index

                for letter in phone_letters[digits[index + 1]]:
                    stack.append(combination + letter)
                    print(combination + letter)
        
        return result
