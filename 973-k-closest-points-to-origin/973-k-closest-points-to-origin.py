class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [a ** 2 + b ** 2 for a, b in points]
        newind = list(zip(points, dist))
        def quicksort(begin, end):
            if begin >= end:
                return
            i, j = begin, end
            pivoind = random.randrange(i, j + 1)
            newind[i], newind[pivoind] = newind[pivoind], newind[i]
            pivot = newind[i]
            while i < j:
                while i < j and newind[j][1] >= pivot[1]:  #### caution this equal sign
                    j -= 1
                newind[i] = newind[j]
                while i < j and newind[i][1] <= pivot[1]:
                    i += 1
                newind[j] = newind[i]
            newind[i] = pivot
            if i > k - 1:
                quicksort(begin, i - 1)
            elif i < k - 1:
                quicksort(i + 1, end)
        quicksort(0, len(points) - 1)
        return list(zip(* newind[:k]))[0]