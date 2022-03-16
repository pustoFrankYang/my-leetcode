class Solution:
    # ¡¡¡¡gesah, greedy with simulation?
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        cntpop = 0
        stk = []
        for x in pushed:
            stk.append(x)
            while stk and stk[-1] == popped[cntpop]:
                stk.pop()
                cntpop += 1
        return not len(stk) # or can also:: return cntpop == len(popped)