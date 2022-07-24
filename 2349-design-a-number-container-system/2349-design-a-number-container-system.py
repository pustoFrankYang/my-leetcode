# Q2349m, runtime 14.29%
class NumberContainers:

    def __init__(self):
        self.n2i = {}
        self.i2n = {}
        

    def change(self, index: int, number: int) -> None:
        if index not in self.i2n:
            self.i2n[index] = number
        else:
            prevn = self.i2n[index]
            self.i2n[index] = number
            
            i = bisect.bisect_left(self.n2i[prevn], index)
            del self.n2i[prevn][i]
            
        if number not in self.n2i:
            self.n2i[number] = []
            
        i = bisect.bisect_left(self.n2i[number], index)
        if i == len(self.n2i[number]):
            self.n2i[number].append(index)
        elif self.n2i[number][i] != index:
            self.n2i[number].insert(i, index)
        

    def find(self, number: int) -> int:
        if number not in self.n2i or len(self.n2i[number]) <= 0:
            return -1
        return self.n2i[number][0]
        

# TLE
'''
    def __init__(self):
        self.n2i = {}
        self.i2n = {}
        

    def change(self, index: int, number: int) -> None:
        if index not in self.i2n:
            self.i2n[index] = number
        else:
            prevn = self.i2n[index]
            self.i2n[index] = number
            self.n2i[prevn].remove(index)
            heapq.heapify(self.n2i[prevn])
        if number not in self.n2i:
            self.n2i[number] = []
            heapq.heapify(self.n2i[number])
        heapq.heappush(self.n2i[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.n2i or len(self.n2i[number]) <= 0:
            return -1
        return self.n2i[number][0]
'''


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)