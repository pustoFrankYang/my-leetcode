// ¡¡¡gesah!!! soll studieren
class Solution {
public:
    vector<long long> minCost(int n, vector<vector<int>>& roads, vector<int>& appleCost, int k) {
        // min cost to buy an apple from wherever
        vector<long long> min_costs(n, -1);
        vector<vector<vector<int>>> edges(n, vector<vector<int>>());
        for (auto road : roads) {
            edges[road[0] - 1].push_back({road[1] - 1, road[2]});
            edges[road[1] - 1].push_back({road[0] - 1, road[2]});
        }
        
        // the possible min costs parts
        // pass `greater` so min cost comes first
        // elements are `pair`s, { cost, node }
        priority_queue<pair<long long, long long>, vector<pair<long long, long long>>, greater<>> pq;
        // init pq so that every node buy from themselves
        // so we an start from at least one correct answer
        for (int i = 0; i < n; i ++)
            pq.push({appleCost[i], i});
        
        // Dijkstra iter begins
        while (pq.size() > 0) {
            auto curr = pq.top();
            pq.pop();
            // if the `min_cost` of this node is already calculated,
            // then this path is no longer best, discard
            if (min_costs[curr.second] != -1) continue; 
            // else, this curr.first is the best cost, store it
            min_costs[curr.second] = curr.first;
            
            // use this best cost to update paths to all the neioghbours
            for (auto nxt : edges[curr.second]) {
                // if min_cost of this nxt is already determined before,
                // then already appeared in the pq once
                if (min_costs[nxt[0]] != -1) continue;
                
                pq.push({ curr.first + (1 + k) * nxt[1], nxt[0] });
            }
        }
        
        return min_costs;
    }
};