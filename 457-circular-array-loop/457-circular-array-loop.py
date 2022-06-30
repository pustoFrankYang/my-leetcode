# Q457, runtime 76.53%
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            # no visited, let's check cycle
            f = s = i
            while nums[(f + nums[f]) % n] * nums[f] > 0:
                f = (f + nums[f]) % n
                visited[f] = 1
                if nums[(f + nums[f]) % n] * nums[f] < 0:
                    break
                elif f == s:
                    # length
                    if (f + nums[f]) % n != f: return True
                    else: break
                        
                f = (f + nums[f]) % n
                visited[f] = 1
                if nums[(f + nums[f]) % n] * nums[f] < 0:
                    break
                elif f == s:
                    # length
                    if (f + nums[f]) % n != f: return True
                    else: break
                    
                s = (s + nums[s]) % n
        return False
        
'''
WA:
[-1,-2,-3,-4,-5]

# loop end indent wrong
[3,1,2]
'''