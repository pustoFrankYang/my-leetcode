class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for num in arr:
            m[num] = m.get(num, 0) + 1
        occurrences = list(m.values())
        return len(occurrences) == len(set(occurrences))