class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int ans = 0;
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; i ++) {
            for (int j = i + 1; j < n - 1; j ++) {
                int complement = target - nums[i] - nums[j];
                int idx = Arrays.binarySearch(nums, j + 1, n - 1, complement);
                // System.out.println(idx);
                int hi = idx >= 0 ? idx : -idx;
                int lo = hi - 1;
                // System.out.println("" + i + j + lo);
                while (lo > j && nums[lo] >= complement) lo --;
                if (lo > j && nums[lo] < complement)
                    ans += lo - j;
            }
        }
        return ans;
    }
}

/*
[-1,1,-1,-1]
-1
*/