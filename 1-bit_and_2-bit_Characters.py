"""
Question

We have two special characters:
    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.
"""
#Solution

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # if bits[i] == 1, its the start of 2 bit char. Hence we skip the next bit as its not required to check
        # if bits[i] == 0, its a single char as we skipped the 0 from the 2 bit char earlier.
        # If the second to last is 1, then the last 0 is for a 2 bit char else its a 1 bit char
        
        i = 0
        second_to_last = 0
        
        while i < len(bits):
            if bits[i] == 1:
                second_to_last = 1
                i += 2
            elif bits[i] == 0:
                second_to_last = 0
                i += 1
        return second_to_last == 0