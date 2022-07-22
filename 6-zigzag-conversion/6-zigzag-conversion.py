class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        direction = -1  # lil trick
        curr_row = 0
        for ch in s:
            rows[curr_row].append(ch)
            if curr_row == numRows - 1 or curr_row == 0:
                direction = -direction
            curr_row += direction
        return ''.join(''.join(e) for e in rows)