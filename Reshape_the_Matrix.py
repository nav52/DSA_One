"""
Question

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
#Solution

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ## INTUITION
        # we can see that for final matrix, 
        #   col_idx will increase from 0 to c-1
        #   row_idx will increase only after adding c elements
        # We can mimic this behaviour using math operators % and //.
        
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        num_of_elem = 0
        out_mat = []
        
        for _ in range(r):
            out_mat.append([0]*c)
        
        for i in range(m):
            for j in range(n):
                row_idx = num_of_elem // c
                col_idx = num_of_elem % c
                out_mat[row_idx][col_idx] = mat[i][j]
                num_of_elem += 1
        return out_mat
        