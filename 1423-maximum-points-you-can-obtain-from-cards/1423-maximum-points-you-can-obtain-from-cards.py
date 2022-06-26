class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # just fixed window,in the middle, min
        p, q = 0, len(cardPoints) - k
        curr = sum(cardPoints[:q])
        curmin = curr
        while q < len(cardPoints):
            curr -= cardPoints[p]
            p += 1
            curr += cardPoints[q]
            q += 1
            curmin = min(curr, curmin)
        return sum(cardPoints) - curmin