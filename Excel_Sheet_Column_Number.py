"""
Question

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701

"""
# Solution

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # Plan:
            # If columnTitle = 'AB' the result will be A_index * 26 + B_index = 26 + 2 = 28.
            # If instead columnTitle = 'MRY' the result will be M_index * 26^2 + R_index * 26 + Y_index = 9281.
            # Hence, take the length and multiply its power of 26 to index of each letter in the title.
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lengthOfTitle = len(columnTitle)
        columnNumber = 0
        for letter in columnTitle:
            columnNumber += (alphabet.index(letter)+1) * (26**(lengthOfTitle-1))
            lengthOfTitle -= 1
        return columnNumber