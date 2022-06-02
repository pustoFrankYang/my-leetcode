class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m2 = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if i >= j:
                m2[j][i] = matrix[i][j]
        return m2