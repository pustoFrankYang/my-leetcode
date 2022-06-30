// ¡¡¡ gesah aber warum Median
class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int ans = 0, med = nums[nums.length / 2];
        for (int n : nums) {
            ans += Math.abs(n - med);
        }
        return ans;
    }
}