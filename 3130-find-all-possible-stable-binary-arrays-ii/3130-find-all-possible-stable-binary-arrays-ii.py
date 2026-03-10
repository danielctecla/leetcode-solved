class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        def comp(i):
            ways = [0] * (i + 1)
            prev = [0] * (i + 1)
            prev[0] = 1
            for k in range(1, i + 1):
                curr = [0] * (i + 1)
                pref = 0
                left = 0
                for j in range(1, i + 1):
                    pref = (pref + prev[j - 1]) % mod
                    if j - limit - 1 >= 0:
                        pref = (pref - prev[j - limit - 1]) % mod
                    curr[j] = pref
                ways[k] = curr[i]
                prev = curr
            return ways
        Zero = comp(zero)
        One = comp(one)
        ans = 0
        for a in range(1, zero + 1):
            if a <= one:
                ans = (ans + Zero[a] * One[a]) % mod
            if a - 1 >= 1 and a - 1 <= one:
                ans = (ans + Zero[a] * One[a - 1]) % mod

        for a in range(1, zero + 1):
            if a <= one:
                ans = (ans + Zero[a] * One[a]) % mod
            if a + 1 <= one:
                ans = (ans + Zero[a] * One[a + 1]) % mod

        return ans % mod