# Q54m, 80.54%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range((min(m, n) + 1) // 2):
            for j in range(i, n - i):
                ans.append(matrix[i][j])
            
            for j in range(i + 1, m - i): # 1 less
                ans.append(matrix[j][n - i - 1])
            if min(m, n) - i - i == 1:  # avoid repeat
                break
            for j in range(n - i - 2, i - 1, -1): # 1 less
                ans.append(matrix[m - i - 1][j])
            for j in range(m - i - 2, i, -1): # 1 less
                ans.append(matrix[j][i])
        return ans