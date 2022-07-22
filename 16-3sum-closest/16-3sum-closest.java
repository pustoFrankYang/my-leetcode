// ¡¡¡gesah für binäre Suche
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int ans = nums[0] + nums[1] + nums[2];
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2 && ans != target; i ++) {
            for (int j = i + 1; j < n - 1; j ++) {
                int complement = target - nums[i] - nums[j];
                int idx = Arrays.binarySearch(nums, j + 1, n - 1, complement);
                int hi = idx >= 0 ? idx : -idx;
                int lo = hi - 1;
                if (hi < n && Math.abs(complement - nums[hi]) < Math.abs(target - ans))
                    ans = nums[i] + nums[j] + nums[hi];
                if (lo < n && Math.abs(complement - nums[lo]) < Math.abs(target - ans))
                    ans = nums[i] + nums[j] + nums[lo];
            }
        }
        return ans;
    }
}