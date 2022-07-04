# Q135h, runtime 28.80%
class Solution:
    # holy shayise i've the hard ganz
    # consider these 4 states:
    # \   \  /    /\    \
    #  \   \/    /  \    \
    # all about max of cnt of consecutive ascending
    # elements iter from left and from right
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # record order of ascending from left & r.
        ls, rs = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] - ratings[i - 1] > 0:
                ls[i] = ls[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] - ratings[i + 1] > 0:
                rs[i] = rs[i + 1] + 1
        return sum([max(ls[i], rs[i]) for i in range(n)])