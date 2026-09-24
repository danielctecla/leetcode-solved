class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        required = {}
        for char in t:
            required[char] = required.get(char, 0) + 1

        window = {char: 0 for char in required}

        formed = 0
        required_count = len(required)

        left = 0
        right = 0

        best_start = 0
        best_len = float("inf")

        while right < len(s):
            char = s[right]

            if char in required:
                window[char] += 1

                if window[char] == required[char]:
                    formed += 1

            while formed == required_count:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_char = s[left]

                if left_char in required:
                    window[left_char] -= 1

                    if window[left_char] < required[left_char]:
                        formed -= 1

                left += 1

            right += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]