# ¡¡¡¡gesah! ... diese DP zu klug
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        @cache
        def ans(pos, carpets):
            if pos < 0:
                return 0
            res = ans(pos-1, carpets)+(floor[pos]=='1')
            if carpets:
                res = min(res, ans(pos-carpetLen, carpets-1))
            return res
        return ans(len(floor)-1, numCarpets)

#     def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
#         n = len(floor)
        
#         # dp[i][j] := result of first `i` tiles and using `j` carpets
        
#         # init `i` == 0 to 0 cuz no any tile visible
#         dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]
            
#         for i in range(1, n + 1):
#             for j in range(0, numCarpets + 1):
                
#                 # option 0: use no new carpet
#                 #   add current tile, i.e. +1 when curr tile is white
#                 jump = dp[i - 1][j] + 1 if floor[i - 1] == '1' else dp[i - 1][j]
                
#                 # option 1: use new carpet
#                 #   put in front of curr tile
#                 #   when `i` is at beginning tiles, put carpet at 0;
#                 cover = dp[max(i - carpetLen, 0)][j - 1] if j != 0 else 1005
#                 dp[i][j] = min(cover, jump)
#         return dp[-1][-1]