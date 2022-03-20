'''
WA
[1,2,1,1,1,2,2,2]
[2,1,2,2,2,2,2,2]
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # 1. turning should not more than a half
        # 2. must be one of tops[0] of bottoms[0]
        lth = len(tops)
        
        def minRotOfNum(n):
            # to top
            rot4top = 0
            rot4bot = 0
            for i in range(lth):
                if tops[i] == n and bottoms[i] != n:
                    rot4bot += 1
                if bottoms[i] == n and tops[i] != n:
                    rot4top += 1
                if tops[i] != n and bottoms[i] != n:
                    return -1
                # last cond is both ==, and no plus
            return min(rot4top, rot4bot)
        
        ans0 = minRotOfNum(tops[0])
        ans1 = minRotOfNum(bottoms[0])
        
        if ans0 == -1:
            return ans1
        elif ans1 == -1:
            return ans0
        else:
            return min(ans0, ans1)