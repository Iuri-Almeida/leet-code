class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:][-1::-1]
        if len(b) != 32: b += '0' * (32 - len(b))
        return int(b, 2)