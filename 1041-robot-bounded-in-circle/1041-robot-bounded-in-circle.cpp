class Solution {
public:
    bool isRobotBounded(string instructions) {
        int currx = 0, curry = 0, currdir = 0;
        // dirs arranged to clockwise
        vector<pair<int, int>> dirs = {
            {0, 1}, {1, 0}, {0, -1}, {-1, 0},
        };
        for (int i = 0; i < 4; ++i) {
            for (const char& ch : instructions) {
                switch (ch) {
                    case 'G': 
                        currx += dirs[currdir].first;
                        curry += dirs[currdir].second;
                        break;
                    case 'L':
                        // 记得这里直接减的话取模会取到负数
                        currdir = (currdir - 1 + 4) % 4;
                        break;
                    case 'R':
                        currdir = (currdir + 1) % 4;
                        break;
                }
            }
        }
        return currx == 0 && curry == 0;
    }
};