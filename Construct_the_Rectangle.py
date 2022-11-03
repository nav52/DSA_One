"""
Question

A web developer needs to know how to design a web page's size. 
So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

    The area of the rectangular web page you designed must equal to the given target area.
    The width W should not be larger than the length L, which means L >= W.
    The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example 1:

Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Example 2:

Input: area = 37
Output: [37,1]

Example 3:

Input: area = 122122
Output: [427,286]

Constraints:

1 <= area <= 107
"""
#Solution

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # to meet the requirements of point 3, getting closest to the center,
        # the square root will get as close to the center as possible
        mid = int(math.sqrt(area))
        
        # consider mid to be W here, and until you get to a point where there
        # are exact integers that will equate to a rectangle with area, subtract from mid/W
        # because point 2 states that L >= W
        while area % mid != 0:
            mid -= 1
    
        # compute L from W (mid), and W (mid)
        return [int(area/mid),mid]