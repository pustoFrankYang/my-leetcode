// Q259m, runtime 8.14%
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int ans = 0;
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; i ++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[l] + nums[r];
                if (sum >= target - nums[i]) {
                    r --;
                } else {
                    ans += r - l;
                    l ++;
                }
            }
        }
        return ans;
    }
}

/*
[-1,1,-1,-1]
-1
*/