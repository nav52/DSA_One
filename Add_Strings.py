"""
Question

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
#Solution

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str_to_num(n):
            int_map = {'0':0, '1':1, '2':2, 
                        '3':3, '4':4, '5':5, 
                        '6':6, '7':7, '8':8, '9':9}
            num = 0
            for i in n:
                num = num*10+int_map[i]
            
            return num
        
        return str(str_to_num(num1)+str_to_num(num2))
        