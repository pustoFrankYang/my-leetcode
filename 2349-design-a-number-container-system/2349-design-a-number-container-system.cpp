#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

class NumberContainers {
private:
    unordered_map<int, vector<int>> n2i;
    unordered_map<int, int> i2n;

public:
    NumberContainers() {}

    void change(int index, int number) {
        if (i2n.find(index) == i2n.end()) {
            i2n[index] = number;
        } else {
            int prevn = i2n[index];
            i2n[index] = number;
            
            auto it = lower_bound(n2i[prevn].begin(), n2i[prevn].end(), index);
            n2i[prevn].erase(it);
        }
        
        if (n2i.find(number) == n2i.end()) {
            n2i[number] = vector<int>();
        }
        
        auto it = lower_bound(n2i[number].begin(), n2i[number].end(), index);
        if (it == n2i[number].end() || *it != index) {
            n2i[number].insert(it, index);
        }
    }

    int find(int number) {
        if (n2i.find(number) == n2i.end() || n2i[number].empty()) {
            return -1;
        }
        return n2i[number][0];
    }
};


/***


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

***/