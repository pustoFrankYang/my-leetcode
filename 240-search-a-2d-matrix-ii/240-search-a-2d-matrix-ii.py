# Q240m, runtime 26.45%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # caution how to extract a column
        maxrow = bisect.bisect_right([r[0] for r in matrix], target)
        minrow = bisect.bisect_left([r[-1] for r in matrix], target)
        if minrow < 0: minrow = 0
        if maxrow >= m: maxrow = m - 1
        
        for r in range(minrow, maxrow + 1):
            ind = bisect.bisect_left(matrix[r], target)
            if ind < n and matrix[r][ind] == target:
                return True
        return False
    
    
    
    
    
    
'''
[[1,3,5]]
5
'''