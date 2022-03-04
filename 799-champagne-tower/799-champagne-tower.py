'''
WA
1
0
0
'''
class Solution:
    # ¡¡¡¡gesah... to find the solution also simulates, 
    # so that every col in every row pours to next layer
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [0] * 101
        nex = [0] * 101
        prev[0] = poured  #### must done outsidem loop
        for r in range(query_row):
            for c in range(r + 1):
                adder = max(0, (prev[c] - 1) / 2)
                nex[c] += adder
                nex[c + 1] += adder
            prev = nex
            nex = [0] * 101
        return min(1, prev[query_glass])  ## no large than 1!