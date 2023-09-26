 
class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        int ans = 0;
        unordered_map<int, vector<int>> dirs, rev_dirs;
        bool v[50000 + 5] = { false };
        for (auto conn : connections) {
            if (dirs.contains(conn[0]))
                dirs[conn[0]].emplace_back(conn[1]);
            else
                dirs[conn[0]] = vector{conn[1]};
            
            if (rev_dirs.contains(conn[1]))
                rev_dirs[conn[1]].emplace_back(conn[0]);
            else
                rev_dirs[conn[1]] = vector{conn[0]};
        }
        queue<int> q({0});
        v[0] = true;
        while (q.size()) {
            int curr = q.front();
            q.pop();
            for (int next : dirs[curr]) {
                if (!v[next]) {
                    v[next] = true;
                    q.push(next);
                    ans ++;
                }
            }
            for (int next : rev_dirs[curr]) {
                if (!v[next]) {
                    v[next] = true;
                    q.push(next);
                }
            }
        }
        return ans;
    }
};