# Q2347e, runtime
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks.sort()
        if all(suits[0] == suit for suit in suits):
            return 'Flush'
        if ranks[0] == ranks[1] == ranks[2] or ranks[1] == ranks[2] == ranks[3] or ranks[2] == ranks[3] == ranks[4]:
            return 'Three of a Kind'
        if ranks[0] == ranks[1] or ranks[1] == ranks[2] or ranks[2] == ranks[3] or ranks[3] == ranks[4]:
            return 'Pair'
        return 'High Card'