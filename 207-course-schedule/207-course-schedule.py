# Q207m, runtime 22.96%, py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [set() for _ in range(numCourses)]
        invpres = [set() for _ in range(numCourses)]
        cnt = 0
        for preq in prerequisites:
            preqs[preq[0]].add(preq[1])
            invpres[preq[1]].add(preq[0])
            cnt += 1
        q = []
        for i in range(len(preqs)):
            if len(preqs[i]) == 0:
                q.append(i)
        while len(q):
            curr = q.pop(0)
            for i in invpres[curr]:
                preqs[i].remove(curr)
                cnt -= 1
                if len(preqs[i]) == 0:
                    q.append(i)
        return False if cnt else True