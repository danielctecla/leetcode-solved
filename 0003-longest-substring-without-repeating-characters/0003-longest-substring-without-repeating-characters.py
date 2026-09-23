class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # maximum length
        # empty string?
        # only letters? No, digits, spaces, etc.

        # I think a brute force.
        # n^2 solution - time complexity
        # 1 - time complexity

        # Start in 0 and end in len(s) - 1
        #   for each iteration we use a empty set
        #   if exist the value we pass to the next iteration
        #   if not we still growing the "window" or the substring
        #   all the time we check if the current is bigger than than the old state saved
        
        # only at the most 100 characters so the time complexity is O(n*100) - n
        # abcdefgaiuoe

        # I founded a better approach and it's using sliding window. Using slading window I remove elements until two characters doesn't exist.
        # left = 0
        # right = 0
        # while, right is not at the end
        #   if the right is not in the set
        #       add to the set
        #       we move the right pointer
        #       check if the current len(set) is bigger than the saved and keep it
        #   else
        #       delete left from the set
        #       we move left
        #   return maximum len

        # time complexity - O(n)
        # memory complexity - O(1)
        longest_substring = 0
        n = len(s) 
        left = 0
        right = 0
        current_characters = set()

        while right < n:
            if s[right] not in current_characters:
                current_characters.add(s[right])
                right += 1
                longest_substring = max(longest_substring, len(current_characters))
            else:
                current_characters.remove(s[left])
                left += 1

        return longest_substring

