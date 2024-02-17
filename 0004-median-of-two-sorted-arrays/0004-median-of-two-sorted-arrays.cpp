// ！！！！！仅供复习参考用，用很久之前写的python自动改成的cpp
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> A, B;
        int m = nums1.size(), n = nums2.size();
        if (m > n) {
            A = nums2;
            B = nums1;
            m = nums2.size();
            n = nums1.size();
        } else {
            A = nums1;
            B = nums2;
        }
        int imin = 0, imax = m, isOdd = (m + n) % 2;
        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = (m + n - 2 * i + 1) / 2;
            if (i > 0 && j < n && A[i - 1] > B[j]) {
                imax = i - 1;
            } else if (j > 0 && i < m && B[j - 1] > A[i]) {
                imin = i + 1;
            } else {
                int maxL, minR;
                if (i <= 0) {
                    maxL = B[j - 1];
                } else if (j <= 0) {
                    maxL = A[i - 1];
                } else {
                    maxL = max(B[j - 1], A[i - 1]);
                }
                if (isOdd) {
                    return maxL;
                }
                
                if (i >= m) {
                    minR = B[j];
                } else if (j >= n) {
                    minR = A[i];
                } else {
                    minR = min(B[j], A[i]);
                }
                return (maxL + minR) / 2.0;
            }
        }
        return 0.0;
    }
};
