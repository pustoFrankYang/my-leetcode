# Q207m, runtime, py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [set() for _ in range(numCourses)]
        # cnts = [0] * numCourses
        cnt = 0
        for preq in prerequisites:
            preqs[preq[0]].add(preq[1])
            cnt += 1
            # cnts[preq[0]] += 1
        q = []
        for i in range(len(preqs)):
            if len(preqs[i]) == 0:
                q.append(i)
        while len(q):
            curr = q.pop(0)
            for i in range(numCourses):
                if curr in preqs[i]:
                    preqs[i].remove(curr)
                    cnt -= 1
                    if len(preqs[i]) == 0:
                        q.append(i)
        return False if cnt else True