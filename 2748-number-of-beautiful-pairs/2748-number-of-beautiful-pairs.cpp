class Solution {
public:
    int gcd(int a, int b) {
        if ((a == b && a != 1) || (a % 2 == 0 && b % 2 == 0) || (a % 3 == 0 && b % 3 == 0))
            return 2;
        else
            return 1;
    }
    int countBeautifulPairs(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; i ++){
            int first = nums[i];
            if (first / 1000)
                first = first/1000;
            else if (first / 100)
                first = first / 100;
            else if (first / 10)
                first = first / 10;
            for (int j = i + 1; j < n; j ++) {
                int last = nums[j] % 10;
                printf("%d, %d\n", first, last);
                if (gcd(first, last) == 1)
                    ans ++;
            }
        }
        return ans;
    }
};