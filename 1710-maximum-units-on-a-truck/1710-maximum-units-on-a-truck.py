# Q1710e runtime 39.68%
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        ans = cntbox = 0
        for numbox, unit in boxTypes:
            if cntbox + numbox <= truckSize:
                ans += unit * numbox
                cntbox += numbox
            else:
                ans += unit * (truckSize - cntbox)
                break
        return ans
    
'''
WA
# forgot to return
[[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
35
'''