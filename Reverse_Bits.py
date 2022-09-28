"""
Question

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
so return 3221225471 which its binary representation is 10111111111111111111111111111111.

"""
# Solution
"""
We initialize answer to 0, so in binary it's 32 zeroes.
We loop over 32 times, since every integer is gonna have 32 possible 0/1.
1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, 
    ans << 1 we shift all bits that we already have in our answer to the left, 
    so after this shifting the bit on the right is 0, plus by using + we set the last bit in the answer to the value that we got in n & 1.
2nd line in the loop we shift bits of our initial number n to the right, 
    since we've already checked the last bit of n, 
    so we just move on to the next bit.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n >>= 1
        return res