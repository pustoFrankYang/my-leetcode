class Solution:
    # it will form a loop
    # and no outer element can enter the loop, wegens permutation
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        maxlen = currlen = 0
        for i in range(len(nums)):
            j = i
            while not visited[j]:
                currlen += 1
                visited[j] = 1
                j = nums[j]
            maxlen = max(maxlen, currlen)
            currlen = 0
        return maxlen