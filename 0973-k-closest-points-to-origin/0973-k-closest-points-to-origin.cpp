// ！！！！只是把之前写的代码自动转cpp用来观察复习

#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        return quickSelect(points, k);
    }
    
    vector<vector<int>> quickSelect(vector<vector<int>>& points, int k) {
        int left = 0, right = points.size() - 1;
        int pivotIndex = points.size();
        while (pivotIndex != k) {
            pivotIndex = partition(points, left, right);
            if (pivotIndex < k) {
                left = pivotIndex;
            } else {
                right = pivotIndex - 1;
            }
        }
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
    
    int partition(vector<vector<int>>& points, int left, int right) {
        vector<int> pivot = choosePivot(points, left, right);
        int pivotDist = squaredDistance(pivot);
        while (left < right) {
            if (squaredDistance(points[left]) >= pivotDist) {
                swap(points[left], points[right]);
                right--;
            } else {
                left++;
            }
        }
        if (squaredDistance(points[left]) < pivotDist) {
            left++;
        }
        return left;
    }
    
    vector<int> choosePivot(vector<vector<int>>& points, int left, int right) {
        return points[left + (right - left) / 2];
    }
    
    int squaredDistance(vector<int>& point) {
        return pow(point[0], 2) + pow(point[1], 2);
    }
};
