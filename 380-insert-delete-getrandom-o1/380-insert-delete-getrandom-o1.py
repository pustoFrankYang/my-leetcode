# Q380m, runtime 95.97%
class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        else:
            self.m[val] = len(self.l)
            self.l.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        else:
            self.m[self.l[-1]] = self.m[val]
            self.l[-1], self.l[self.m[val]] = self.l[self.m[val]], self.l[-1]
            del self.m[val]
            self.l.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()