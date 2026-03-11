class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        Xor operation
        when 

        1 xor 1 -> 0
        0 xor 1 -> 1
        """
        if n == 0:
            return 1
            
        mask = (1 << n.bit_length()) - 1
        return n ^ mask

