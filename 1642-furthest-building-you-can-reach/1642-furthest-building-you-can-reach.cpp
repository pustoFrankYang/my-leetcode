class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // 用最小堆，我一开始想复杂了，
        // 以为要动态更新每次的最大k个，
        // 其实只要每次满了都去掉最小的就可以！！！！！！！
        priority_queue<int, vector<int>, ::greater<int>> minHeap;
        if (heights.size() == 1) return 0;
        if (ladders <= 0 && bricks < heights[1] - heights[0]) return 0;
        int i = 1;
        for (i = 1; i < heights.size(); i++) {
            int diff = heights[i] - heights[i - 1];
            if (diff <= 0) continue;
            
            minHeap.push(diff);
            if (minHeap.size() <= ladders) continue;
            bricks -= minHeap.top();
            minHeap.pop();
            if (bricks < 0) break;
        }
        return i - 1;
    }
};